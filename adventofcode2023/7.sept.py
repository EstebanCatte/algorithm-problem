# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:59:43 2023

@author: EC266662
"""


def compter_caracteres(chaine):
    comptes = {}
    for caractere in chaine:
        comptes[caractere] = comptes.get(caractere, 0) + 1
    return comptes

def get_power(compt):
    c = list(compt.keys())
    if len(c) == 5:
        return 0
    if len(c) == 1:
        return 6
    
    compt2 = dict(sorted(compt.items(), key=lambda item: item[1], reverse=True))
    values = list(compt2.values())
    if values[0] == 2 and values[1] == 1:
        return 1
    if values[0] == 2 and values[1] == 2:
        return 2
    if values[0] == 3 and values[1] == 1:
        return 3
    if values[0] == 3 and values[1] == 2:
        return 4
    if values[0] == 4 and values[1] == 1:
        return 5
    
def resolve(chaine1, chaine2):
    powers = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    for i in range(5):
        if powers.index(chaine1[i]) > powers.index(chaine2[i]):
            return chaine1
        if powers.index(chaine1[i]) < powers.index(chaine2[i]):
            return chaine2
    return chaine1
        

def compare(chaine1, chaine2):
    compt1 = compter_caracteres(chaine1)
    compt2 = compter_caracteres(chaine2)
    pow1 = get_power(compt1)
    pow2 = get_power(compt2)
    if pow1 > pow2 :
        return chaine1, chaine2
    if pow1 < pow2:
        return chaine2, chaine1
    if pow1 == pow2:
        res = resolve(chaine1, chaine2)
        if res == chaine1:
            return chaine1,chaine2
        if res == chaine2:
            return chaine2, chaine1
        
        
with open("./input7.txt") as f:
    ls = f.read().strip().split("\n")
    for i,l in enumerate(ls): ls[i]=l.split(" ")

for l in ls:
    for i,l in enumerate(ls[:-1]):
        res = compare(ls[i][0], ls[i+1][0])
        if res[0] == ls[i+1][0]:
            ls[i][0] = res[0]
            ls[i+1][0] = res[1]
            temp = ls[i+1][1]
            ls[i+1][1] = ls[i][1]
            ls[i][1] = temp

res = 0
for i in range(len(ls) - 1, -1, -1):
    print("chaine is = {} with bid {} rank {}".format(ls[i][0], ls[i][1], i))
    res +=  int(ls[i][1]) * (i+1)
    
print(res)

#FOR PART 2; REPLACE JOKER BY HIGHIEST VALUES IN THE LIST WITH THE HIGHEST FREQUENCY





