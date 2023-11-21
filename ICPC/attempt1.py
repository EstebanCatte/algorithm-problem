import math
import numpy as np

class User():

    def __init__(self, id, num_rbg, num_bs, num_tti, num_frame):
        self.id = id
        self.sinr0 = np.zeros((num_bs, num_tti, num_rbg))
        self.status = np.zeros((num_frame, num_tti)) #connected to the 0th basestation
        self.block = 0
        self.tti = 0


class Basestation():

    def __init__(self, id, num_user, num_rbg):
        self.id = id
        self.interf_factor= np.zeros((num_user, num_user, num_rbg))


#TODO: the unsignment

class Solver():

    def __init__(self, users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr, interference):
        self.users = users
        self.basestations = basestations
        self.num_rbg = num_rbg
        self.num_bs = num_bs
        self.num_tti = num_tti
        self.num_frame = num_frame
        self.frames = frames
        self.num_user = num_user

        #matrix init
        self.formate_sinr(sinr)
        self.formate_interf(interference)

        #solution matrix
        self.powers = np.zeros((num_user, num_bs, num_tti, num_rbg ))
        self.sinr = np.zeros((num_user, num_bs, num_tti, num_rbg ))


    def is_communicating(self, user, bs, rbg, tti):
        return self.powers[user.id][bs.id][tti][rbg] > 0


    def allocate_power(self, power_value, user, bs, rbg, tti):
        self.powers[user.id][bs.id][rbg][tti] = np.clip(power_value, 0, 4)


    def compute_all_rbg_interference(self):
        for i,user in self.users:
            self.compute_rbg_interference(user)


    def get_used_rbg(self, user, bs, tti):
        #retourne la liste des blocs sur lequels <user> communique pour une station <bs> et un <tti> donné
        line = self.powers[user.id][bs.id][tti]
        blocks = np.where(line>0)
        return blocks[0]


    def compute_in_interference(self, user, bs, tti, rbg):
        #Interference from the same bs for user and interf_user
        #equation 7 numerator
        interference = 1
        for interf_user in self.users:
            if user != interf_user:
                in_communication = self.is_communicating(interf_user, bs, rbg, tti)
                interf_factor = bs.interf_factor[interf_user.id][user.id][rbg] 
                interference *= math.exp( interf_factor * in_communication)
        return interference


    def compute_out_interference(self, user, bs, tti, rbg):
        #Pénalité de colision parce que user et inter_user communique avec la même bs sur le même bloc et tti
        #Interference from the other bs communicating
        #equation 7 denominator
        interference = 0
        for interf_bs in self.basestations:
            if interf_bs != bs:
                for interf_user in self.users:
                    if interf_user != user:
                        interf_factor = interf_bs.interf_factor[interf_user.id][user.id][rbg]
                        sinr0 = user.sinr0[interf_bs.id][tti][rbg]
                        power = self.powers[interf_user.id][interf_bs.id][tti][rbg]
                        interference +=  sinr0 * power * math.exp(-interf_factor)
        return interference


    def compute_sinr(self, user , bs, tti, rbg):
        sinr0 = user.sinr0[bs.id][tti][rbg]
        power = self.powers[user.id][bs.id][tti][rbg]
        in_interference = self.compute_in_interference(user, bs, tti, rbg)
        out_interference = self.compute_out_interference(user, bs, tti, rbg)
        sinr =  (sinr0 * power * in_interference) / (1+out_interference)
        print("Com User {} bs {} in_interf = {} et out_interf = {}".format(user.id, bs.id, in_interference, out_interference))
        self.sinr[user.id][bs.id][tti][rbg] = sinr
        return sinr


    def compute_geometric_sinr(self, user , bs, tti):
        #eq 6
        produit = 1
        blocks = self.get_used_rbg(user, bs, tti)
        for i in blocks:    
            produit *= self.compute_sinr(user, bs, tti, i)
        #len(block) is the number of block utilized for station k
        return produit**(1/ max(1,len(blocks)))


    def compute_rate(self, frame):
        W = 192
        rate = 0
        user = self.users[frame["userid"]]
        for tti in range(self.num_tti):
            for bs in self.basestations:
                for rbg in range(self.num_rbg):
                    in_com = self.is_communicating(user, bs, rbg, tti)
                    sinr = self.compute_geometric_sinr(user, bs, tti)
                    rate += in_com * math.log2(1+sinr)
        rate = W*rate
        frame["rate"] = rate


    def check_frame_validity(self, frame):
        return frame["rate"] > frame["TBS"]


    #Met bien en forme l'input
    def formate_sinr(self, sinr):
        #see input pour l'ordre
        for t in range(self.num_tti):
            for b in range(self.num_bs):
                for r in range(self.num_rbg):
                    for i, user in enumerate(self.users):
                        user.sinr0[b][t][r] = sinr[r + b*num_rbg + t*num_bs*num_rbg][i]

    
    def formate_interf(self, interference):
        #see input pour l'ordre
        for i,bs in enumerate(self.basestations):
            for r in range(self.num_rbg):
                for u in range(self.num_user):
                    for j in range(self.num_user):
                        bs.interf_factor[u][j][r] = interference[u + r*num_user + i*num_rbg*num_user][j]
    

    def network_status(self):
        np.zeros((num_user, num_bs, num_tti, num_rbg ))
        for u in self.users:
            for bs in self.basestations:
                for t in range(self.num_tti):
                    for r in range(self.num_rbg):
                        p = self.powers[u.id][bs.id][t][r]
                        sinr = self.sinr[u.id][bs.id][t][r]
                        if p > 0:
                            print("BS {} sending to UE {} with block {} and TTI {}".format(bs.id, u.id, t, r))
                        print("===SINR === BS {} sending to UE {} with block {} and TTI {} = {}".format(bs.id, u.id, t, r, sinr))


#==========================================================================
#                       INPUTS INPUTS INPUTS
#==========================================================================
#1 TTI is 0.5ms
#Number of USER
#users are numbered from 0 to N-1
#num_user = int(input())


#Number of cell
#cell are numbered from 0 to K-1
#each of which is equipped with a base station to serve users.
#One base station usually serves multiple users, and multiple base stations may serve one user at the same time.
#num_bs = int(input())


#TTI number
#Transmission Time Interval
#numbered from 0 to T-1
#num_tti = int(input())


#RBD number
#Each RBG coresponds to a transmission bandwidth of 5760 kHz
#numbered from 0 to T-1
#num_rbg = int(input())


#Initial Signal-to-Interference-plus-Noise-Ratio
# sinr = []
# for i in range(5, 5+num_rbg*num_bs*num_tti):
#     sinr.append(list(map(float, input().split())))


#interference factor
# interference = []
# for i in range(5+num_rbg*num_bs*num_tti, 5+num_rbg*num_bs*num_tti + num_user*num_rbg*num_bs):
#     interference.append(list(map(float, input().split())))


#Number of frame
# num_frame = int(input())
# frame = []
# for i in range(num_frame):
#     inp = list(map(float, input().split()))
#     frame.append({"frameid": inp[0], #frame id 0 to J-1 increasing order
#                 "TBS": inp[1], #size TBS
#                 "userid": inp[2], #user ID it belongs to
#                 "t0": inp[3], #first tti from 0 to T-1
#                 "tti": inp[4], #number of TTI
#                 "t1": inp[3]+inp[4]}) 

#==========================================================================
#                       TEST
#==========================================================================
frames = []
num_user = 2
num_bs = 2
num_tti = 2
num_rbg = 1
sinr = [[1.38, 11.38], [1.38, 11.38], [2.38, 2.38], [2.38, 2.38]]
interference = [[0,-2], [-2, 0], [0, -2], [-2, 0]]
num_frame = 2
inpu = ["0 250 0 0 2", "1 25 1 0 2"]
for i in range(num_frame):
    inp = list(map(float, inpu[i].split()))
    #cette ligne peut ne pas avoir de sens
    if inp[4] > 1: 
        frames.append({"frameid": int(inp[0]), #frame id 0 to J-1 increasing order
                    "TBS": inp[1], #size TBS
                    "userid": int(inp[2]), #user ID it belongs to
                    "t0": inp[3], #first tti from 0 to T-1
                    "tti": inp[4], #number of TTI
                    "t1": inp[3]+inp[4]-1,
                    "rate":0}) 
#==========================================================================
#                       Start
#==========================================================================
users = [User(i, num_rbg, num_bs, num_tti, num_frame) for i in range(num_user)]
basestations = [Basestation(i, num_user, num_rbg) for i in range(num_bs)]

solver = Solver(users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr, interference)

#self.powers = np.zeros((num_user, num_bs, num_tti, num_rbg ))
solver.powers[1][0][0][0] = 0.004950
solver.powers[1][1][0][0] = 0.004950
solver.powers[0][0][1][0] = 0.245039
solver.powers[0][1][1][0] = 0.245039

solver.compute_rate(frames[0])
solver.compute_rate(frames[1])
for i in range(num_frame):
    print("Frame {} TBS {} Rate {}".format(i, frames[i]["TBS"], frames[i]["rate"]))
    print("Frame {} check: {}".format(i, solver.check_frame_validity(frames[0])))


#on peut trier les frames par difficulté en terme de TBS


#Output for a certain input is the optimization result of p(k)rnt (float), which has R⋅K⋅T
#lines. Each line has N elements, corresponding to N users. 
# p(k)rnt is the (n+1) -th element of line (1+r+k⋅R+t⋅K⋅R)
# /!\ 
#p(k)rnt is a nonnegative continuous variable denoting the power allocated to user n in the r-th RBG of cell k at TTI t
#determiner la puissance au User N dans le RBG r de la BS k au TTI t
# /!\ 

#We have 0 < p(k)rnt < 4 and each cell must respect sum(p(k)nrt) < R
