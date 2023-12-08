# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:31:40 2023

@author: EC266662
"""
#===============================PART 1======================
# with open("./input8.txt") as f:
#     ls = f.read().strip().split("\n")
    
# instruction = ls[0]
# final = []
# for i,l in enumerate(ls[2:]): 
#     ls[i+2] = l.split(' ')
#     final.append([ls[i+2][0] , ls[i+2][2][1:-1], ls[i+2][3][:-1]])

# def find(chaine, final):
#     for i,f in enumerate(final):
#         if f[0] == chaine:
#             index = i
#     return index

# cur = 'AAA'
# index = find(cur, final)
# num = 0
# while 1:
#     for i in instruction:
#         num+=1
#         print("current pos {} index {}".format(cur, index))
#         if i == 'R':
#             cur = final[index][2]
#             index = find(cur, final)
#         if i == 'L':
#             cur = final[index][1]
#             index = find(cur, final)
#         if cur == 'ZZZ':
#             input(num)
#             stop = 0
#             break
    
#===============================PART 2======================
with open("./input8.txt") as f:
    ls = f.read().strip().split("\n")
    
instruction = ls[0]
final = []
for i,l in enumerate(ls[2:]): 
    ls[i+2] = l.split(' ')
    final.append([ls[i+2][0] , ls[i+2][2][1:-1], ls[i+2][3][:-1]])


def find(chaine, final):
    for i,f in enumerate(final):
        if f[0] == chaine:
            index = i
    return index

def start_points(final):
    starts = []
    curs = []
    for i,f in enumerate(final):
        if f[0][-1] == 'A':
            starts.append(i)
            curs.append(f[0])
    return starts, curs
    
def check_fin(curs):
    for cur in curs:
        if cur[-1] != 'Z':
            return False
    return True
    
starts, curs = start_points(final)
num = 0
while 1:
    for j in instruction:
        num+=1
        print("Curs state : {}".format(curs))
        print("Start state : {}".format(starts))
        for i,cur in enumerate(curs):
            if j == 'R':
                curs[i] = final[starts[i]][2]
                starts[i] = find(cur, final)
            if j == 'L':
                curs[i] = final[starts[i]][1]
                starts[i] = find(cur, final)
            if check_fin(curs):
                input(num)
                stop = 0
                break
        
    
# ll = [x for x in open("./input8.txt").read().strip().split('\n\n')]
# import math
# inst = list(ll[0])
# conn = {}
# for l in ll[1].split("\n"):
# 	a = l.split(" ")[0]
# 	b = l.split("(")[1].split(",")[0]
# 	c = l.split(" ")[3].split(")")[0]
# 	conn[a] = (b, c)
# pos = 'AAA'
# idx = 0
# while pos != 'ZZZ':
# 	d = inst[idx%len(inst)]
# 	pos = conn[pos][0 if d=='L' else 1]
# 	idx += 1
# print("p1", idx)
# def solvesteps(start):
# 	pos = start
# 	idx = 0
# 	while not pos.endswith('Z'):
# 		d = inst[idx%len(inst)]
# 		pos = conn[pos][0 if d=='L' else 1]
# 		idx += 1
# 	return idx
# ret = 1
# for start in conn:
# 	if start.endswith('A'):
# 		ret = math.lcm(ret, solvesteps(start))
# print("p2", ret)
    