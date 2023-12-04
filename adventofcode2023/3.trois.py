import math as m, re

board = list(open('H:/alg/algorithm-problem/adventofcode2023/input3.txt'))

#find all symbols positions

chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}


#finds all number in the grid
for r, row in enumerate(board):
    #\d is for any digit between [0,9]
    #"+" is to tell to continue the research through all digits
    for n in re.finditer(r'\d+', row):
        #for each number create a sed of edge coordinate
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}
        
        #On regarde si dans un edge il y a un symbol qu'on a trouver au début
        for o in edge & chars.keys():
            chars[o].append(int(n.group()))
            #si oui on garde en memoire

print(sum(sum(p)    for p in chars.values()))
#for gears
print(sum(m.prod(p) for p in chars.values() if len(p)==2))


