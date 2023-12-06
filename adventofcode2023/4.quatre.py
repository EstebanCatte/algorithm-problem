import re
with open("H:/alg/algorithm-problem/adventofcode2023/input4.txt") as f:
    ls = f.read().strip().split("\n")

res = 0
matches1 = []
m = []
for l in ls:
    line = l.split(':')[1]
    line = line.split('|')
    a = [n.group() for n in re.finditer(r'\d+', line[0])]
    b = [n.group() for n in re.finditer(r'\d+', line[1])]                                 
    c = [value for value in a if value in b]
    matches1.append(len(c))        
    if len(c) > 0:
        res += 2**(len(c)-1)
        
cards = [1] * len(matches1)
for i, n in enumerate(matches1):
    for j in range(n):
        cards[i + j + 1] += cards[i]
        
print(res)
print(sum(cards))        