# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:01:39 2023

@author: EC266662
"""

with open("./input9.txt") as f:
    ls = f.read().strip().split("\n")
    
    
import time,sys,re,math
tstart=time.time()

with open("./input10.txt") as fi:
    raw= [[x for x in l] for l in fi.read().strip().split('\n')]
    S = dict()
    for R in range(len(raw)):
        for C in range(len(raw[0])):
            S[(R,C)] = raw[R][C]
            if raw[R][C] == 'S': start = (R,C)

def move(p,d):
    R,C = p
    dc,dr = [1,0,-1,0],[0,1,0,-1]#0r,1down,2l,3up
    if S[p] == 'S' and d == 0: d = 0
    elif S[p] == 'F' and d == 3: d = 0
    elif S[p] == 'F' and d == 2: d = 1

    elif S[p] == '7' and d == 0: d = 1
    elif S[p] == '7' and d == 3: d = 2

    elif S[p] == 'J' and d == 1: d = 2
    elif S[p] == 'J' and d == 0: d = 3

    elif S[p] == 'L' and d == 2: d = 3
    elif S[p] == 'L' and d == 1: d = 0
    return (R+dr[d],C+dc[d]),d

complete= True
P = set()
pos = start
#starting direction
direction =  0
while complete:
    pos,direction = move(pos,direction)
    if S[pos]== 'S':
        complete = False
    if pos not in P:
        P.add(pos)
print('part1 - finding loop with max distance',len(P)//2)
I = set()
last = ''
for R in range(len(raw)):
    out = True
    for C in range(len(raw[0])):
        if (R,C) in P:
            if S[R,C]!= '-' and last+S[(R,C)] not in ['L7','FJ']:
                out = not out
                last = S[(R,C)]
        else:
            if not out:
                I.add((R,C))
print('part2 - enclosed area:',len(I))
tend=time.time()
print(round(tend-tstart,5))   