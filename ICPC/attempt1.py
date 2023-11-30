import math

class User():

    def __init__(self, id, num_rbg, num_bs, num_tti, num_frame):
        self.id = id
        self.sinr0 = [[[0] * num_bs for _ in range(num_tti)] for _ in range(num_rbg)]
        self.block = 0
        self.tti = 0


class Basestation():

    def __init__(self, id, num_user, num_rbg):
        self.id = id
        self.interf_factor= [[[0] * num_rbg for _ in range(num_user)] for _ in range(num_user)]


#TODO: the unsignment

class Solver():

    def __init__(self, users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr0, interference):
        self.users = users
        self.basestations = basestations
        self.num_rbg = num_rbg
        self.num_bs = num_bs
        self.num_tti = num_tti
        self.num_frame = num_frame
        self.frames = frames
        self.num_user = num_user

        #matrix init
        self.formate_sinr(sinr0)
        self.formate_interf(interference)

        #solution matrix
        self.powers = [[[[0] * num_rbg for _ in range(num_tti)] for _ in range(num_bs)] for _ in range(num_user)]
        self.sinr = [[[[0] * num_rbg for _ in range(num_tti)] for _ in range(num_bs)] for _ in range(num_user)]


    #determine a user is communicating with <bs> at <tti> with <rbg>
    def is_communicating(self, user, bs, rbg, tti):
        return self.powers[user.id][bs.id][tti][rbg] > 0


    def get_used_rbg(self, user, bs, tti):
        #retourne la liste des blocs sur lequels <user> communique pour une station <bs> et un <tti> donné
        line = self.powers[user.id][bs.id][tti]
        blocks = [index for index, value in enumerate(line) if value > 0]
        return blocks


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
                        sinr0 = user.sinr0[rbg][tti][interf_bs.id]
                        power = self.powers[interf_user.id][interf_bs.id][tti][rbg]
                        interference +=  sinr0 * power * math.exp(-interf_factor)
        return interference


    def compute_sinr(self, user , bs, tti, rbg):
        sinr0 = user.sinr0[rbg][tti][bs.id]
        power = self.powers[user.id][bs.id][tti][rbg]
        in_interference = self.compute_in_interference(user, bs, tti, rbg)
        out_interference = self.compute_out_interference(user, bs, tti, rbg)
        sinr =  (sinr0 * power * in_interference) / (1+out_interference)
        #print("Com User {} bs {} in_interf = {} et out_interf = {}".format(user.id, bs.id, in_interference, out_interference))
        self.sinr[user.id][bs.id][tti][rbg] = sinr
        print("sinr0 = {} power = {} in_interf = {} out_interf = {} sinr = {}".format(sinr0, power, in_interference, out_interference, sinr, sinr))
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
        #print("#  ..rate computation..")
        W = 192
        rate = 0
        user = self.users[frame["userid"]]
        for tti in range(self.num_tti):
            for bs in self.basestations:
                for rbg in range(self.num_rbg):
                    in_com = self.is_communicating(user, bs, rbg, tti)
                    sinr = self.compute_geometric_sinr(user, bs, tti)
                    rate += in_com * math.log2(1+sinr)
                    print("| in com {} | sinr {} | rate {}".format(in_com, sinr, rate))
        rate = W*rate
        frame["rate"] = rate


    def check_frame_validity(self, frame):
        # print("...validity check...")
        # print("frame rate : {} | frame tbs : {}".format(frame["rate"], frame["TBS"]))
        # print("check is {}".format(frame["rate"] >= frame["TBS"]))
        return frame["rate"] >= frame["TBS"]


    #Met bien en forme l'input
    def formate_sinr(self, sinr):
        #see input pour l'ordre
        for t in range(self.num_tti):
            for b in range(self.num_bs):
                for r in range(self.num_rbg):
                    for i, user in enumerate(self.users):
                        user.sinr0[r][t][b] = sinr[r + b*num_rbg + t*num_bs*num_rbg][i]

    
    def formate_interf(self, interference):
        #see input pour l'ordre
        for i,bs in enumerate(self.basestations):
            for r in range(self.num_rbg):
                for u in range(self.num_user):
                    for j in range(self.num_user):
                        bs.interf_factor[u][j][r] = interference[u + r*num_user + i*num_rbg*num_user][j]
    

    def network_status(self):
        for u in self.users:
            for bs in self.basestations:
                for t in range(self.num_tti):
                    for r in range(self.num_rbg):
                        p = self.powers[u.id][bs.id][t][r]
                        sinr = self.sinr[u.id][bs.id][t][r]
                        # if p > 0:
                        #     print("BS {} sending to UE {} with block {} and TTI {}".format(bs.id, u.id, r, t))
                        # print("===SINR === BS {} sending to UE {} with block {} and TTI {} = {}".format(bs.id, u.id, t, r, sinr))


    def sort_frames(self, frames):
        sorted_frames = sorted(frames, key=lambda x: x['TBS'])
        return sorted_frames


class Heuristic1(Solver):

    def __init__(self, users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr, interference):
        super().__init__(users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr, interference)

    def find_max_heuristic(self, matrix):
        max_value = float('-inf')
        max_index = None
        for rbg in range(num_rbg):
            for tti in range(num_tti):
                current_value = matrix[rbg][tti]
                if current_value > max_value:
                    max_value = current_value
                    max_index = (rbg, tti)
        return max_index


    def compute_heuristic_matrix(self):
        #metric is sum(sinr0)
        self.heuristic_matrix = [[[0] * num_tti for _ in range(num_rbg)] for _ in range(num_user)]
        for user in self.users:
            for r in range(self.num_rbg):
                for t in range(self.num_tti):
                    self.heuristic_matrix[user.id][r][t] = sum(user.sinr0[r][t])

        return self.heuristic_matrix


    def find_power(self, TBS, user, rbg, tti):
        #FOR 2 BS CASE
        W = 192
        #2% de marge sur le TBS
        cons = 2**((TBS/1.98)/W) 
        lower_sinr = min(user.sinr0[rbg][tti])
        print("cons = {} lower_sinr = {}".format(cons, lower_sinr))
        value = (cons * math.sqrt(1/(lower_sinr**2))*lower_sinr - 1) / lower_sinr
        return value


    def solve(self, frame):
        user = self.users[frame["userid"]]
        heuristic = self.heuristic_matrix[user.id]
        max_index = self.find_max_heuristic(heuristic)
        
        rbg = max_index[0]
        tti = max_index[1]
        
        power_to_allocate = self.find_power(frame["TBS"], user, rbg, tti)
        
        print("......Debug solver.....")
        print("#   user {} | rbg {} | tti {} | score {}".format(user.id, rbg, tti, max(heuristic)))
        print("#  power allocated : {}".format(power_to_allocate))

        # if power_to_allocate < 0:
        #     raise ValueError("Allocated power is negative")

        self.heuristic_matrix[user.id][max_index[0]][max_index[1]] = -1e9
        power_to_allocate = min(self.num_rbg/self.num_bs, power_to_allocate)
        for bs in self.basestations:
            self.powers[user.id][bs.id][tti][rbg] = max(0,min(power_to_allocate, 4))


    def print_results(self):
        for tti in range(self.num_tti):
            for bs in self.basestations:
                for rbg in range(self.num_rbg):
                    for user in self.users:
                        print(self.powers[user.id][bs.id][tti][rbg], end=" ")
                    print("")

#==========================================================================
#                       INPUTS INPUTS INPUTS
#==========================================================================
print("###########################################")
print("                 ICPC")
print("###########################################")
with open('C:/Users/Esteban/Documents/GitHub/algorithm-problem/ICPC/tests/00.txt', 'r') as file:
    lines = file.readlines()

# # 1 TTI is 0.5ms
# # Number of USER
# # users are numbered from 0 to N-1
num_user = int(lines[0].strip())


# # Number of cell
# # cell are numbered from 0 to K-1
# # each of which is equipped with a base station to serve users.
# # One base station usually serves multiple users, and multiple base stations may serve one user at the same time.
num_bs = int(lines[1].strip())


# # TTI number
# # Transmission Time Interval
# # numbered from 0 to T-1
num_tti = int(lines[2].strip())


# # RBD number
# # Each RBG coresponds to a transmission bandwidth of 5760 kHz
# # numbered from 0 to T-1
num_rbg = int(lines[3].strip())


# #Initial Signal-to-Interference-plus-Noise-Ratio
sinr = []
for i in range(4, 4+num_rbg*num_bs*num_tti):
    sinr.append(list(map(float, lines[i].strip().split())))


# interference factor
interference = []
for i in range(4+num_rbg*num_bs*num_tti, 4+num_rbg*num_bs*num_tti + num_user*num_rbg*num_bs):
    interference.append(list(map(float, lines[i].strip().split())))


# # Number of frame
num_frame = int(lines[4+num_rbg*num_bs*num_tti+num_user*num_rbg*num_bs].strip())
frames = []
for i in range(num_frame):
    inp = list(map(float, lines[4+num_rbg*num_bs*num_tti+num_user*num_rbg*num_bs+1+i].split()))
    frames.append({"frameid": int(inp[0]), #frame id 0 to J-1 increasing order
                "TBS": int(inp[1]), #size TBS
                "userid": int(inp[2]), #user ID it belongs to
                "t0": int(inp[3]), #first tti from 0 to T-1
                "tti": int(inp[4]), #number of TTI
                "t1": int(inp[3]+inp[4]),
                "rate":0}) 
#==========================================================================
#                       INPUTS INPUTS INPUTS
#==========================================================================
# # print("###########################################")
# # print("                 ICPC")
# # print("###########################################")
# # 1 TTI is 0.5ms
# # Number of USER
# # users are numbered from 0 to N-1
# num_user = int(input())

 
# # # Number of cell
# # # cell are numbered from 0 to K-1
# # # each of which is equipped with a base station to serve users.
# # # One base station usually serves multiple users, and multiple base stations may serve one user at the same time.
# num_bs = int(input())
 
 
# # # TTI number
# # # Transmission Time Interval
# # # numbered from 0 to T-1
# num_tti = int(input())
 
 
# # # RBD number
# # # Each RBG coresponds to a transmission bandwidth of 5760 kHz
# # # numbered from 0 to T-1
# num_rbg = int(input())
 
 
# # #Initial Signal-to-Interference-plus-Noise-Ratio
# sinr = []
# for i in range(4, 4+num_rbg*num_bs*num_tti):
#     sinr.append(list(map(float, input().split())))
 
 
# # interference factor
# interference = []
# for i in range(4+num_rbg*num_bs*num_tti, 4+num_rbg*num_bs*num_tti + num_user*num_rbg*num_bs):
#     interference.append(list(map(float, input().split())))
 
 
# # # Number of frame
# num_frame = int(input())
# frames = []
# for i in range(num_frame):
#     inp = list(map(float, input().split()))
#     frames.append({"frameid": int(inp[0]), #frame id 0 to J-1 increasing order
#                 "TBS": int(inp[1]), #size TBS
#                 "userid": int(inp[2]), #user ID it belongs to
#                 "t0": int(inp[3]), #first tti from 0 to T-1
#                 "tti": int(inp[4]), #number of TTI
#                 "t1": int(inp[3]+inp[4]),
#                 "rate":0})    
     
#==========================================================================
#                       TEST
#==========================================================================
# print("#  NUM UE : {}".format(num_user))
# print("#  NUM BS : {}".format(num_bs))
# print("#  NUM TTI: {}".format(num_tti))
# print("#  NUM RBG: {}".format(num_rbg))
# print("#  NUM FRA: {}".format(num_frame))
# print("#############################")

#==========================================================================
#                       Start
#==========================================================================
users = [User(i, num_rbg, num_bs, num_tti, num_frame) for i in range(num_user)]
basestations = [Basestation(i, num_user, num_rbg) for i in range(num_bs)]


solver = Heuristic1(users, basestations, num_rbg, num_bs, num_user, num_tti, num_frame, frames, sinr, interference)

#1) trier les frames
sorted_frames = solver.sort_frames(frames)
solver.compute_heuristic_matrix()

score = 0
for frame in sorted_frames:
    solver.solve(frame)
    solver.compute_rate(frame)
    #print("#  Computing frame {} with TBS : {} and rate : {}".format(frame["frameid"], frame["TBS"], frame["rate"]))
    validity = solver.check_frame_validity(frame)
    #print("#  Frame {} check: {}".format(i, validity))
    score += validity
    #input("#  next... ")

# print("###########################################")
# print("                 RESULTS")
# print("###########################################")
solver.print_results()
# print("End score : {}".format(score))