import math

def compute_rate(user):
    W = 192
    k = 0 #cell number
    rate = W * math.log2(1+user.sinr[k])

def compute_sinr(user):
    sinr = initial_sinr * power * prod(math.exp(interference * status))
    sinr = sinr / 1+ Interfe

#1 TTI is 0.5ms
#Number of USER
#users are numbered from 0 to N-1
N = int(input())

#Number of cell
#cell are numbered from 0 to K-1
#each of which is equipped with a base station to serve users.
#One base station usually serves multiple users, and multiple base stations may serve one user at the same time.
K = int(input())

#TTI number
#Transmission Time Interval
#numbered from 0 to T-1
T = int(input())

#RBD number
#Each RBG coresponds to a transmission bandwidth of 5760 kHz
#numbered from 0 to T-1
R = int(input())

#Initial Signal-to-Interference-plus-Noise-Ratio
#
sinr = []
for i in range(5, 5+R*K*T):
    sinr.append(list(map(float, input().split())))

#interference factor
interference = []
for i in range(5+R*K*T, 5+R*K*T + N*R*K):
    interference.append(list(map(float, input().split())))

#Number of frame
J = int(input())
frame = []
for i in range(J):
    inp = list(map(float, input().split()))
    frame.append({"frameid": inp[0], #frame id 0 to J-1 increasing order
                "TBS": inp[1], #size TBS
                "userid": inp[2], #user ID it belongs to
                "t0": inp[3], #first tti from 0 to T-1
                "tti": inp[4], #number of TTI
                "t1": inp[3]+inp[4]}) 

#Output for a certain input is the optimization result of p(k)rnt (float), which has R⋅K⋅T
#lines. Each line has N elements, corresponding to N users. 
# p(k)rnt is the (n+1) -th element of line (1+r+k⋅R+t⋅K⋅R)
# /!\ 
#p(k)rnt is a nonnegative continuous variable denoting the power allocated to user n in the r-th RBG of cell k at TTI t
#determiner la puissance au User N dans le RBG r de la BS k au TTI t
# /!\ 

#We have 0 < p(k)rnt < 4 and each cell must respect sum(p(k)nrt) < R
