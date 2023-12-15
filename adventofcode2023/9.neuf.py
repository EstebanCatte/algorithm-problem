def fonc(tab):
    tab.append([tab[-1][i+1] - tab[-1][i] for i in range(0, len(tab[-1])-1)])
    return tab

with open("./input9.txt") as f:
    ls = f.read().strip().split("\n")
    
solution = 0
solution2 = 0
for line in ls:
    #line = [1,3,6,10,15,21]
    tab = [[int(i) for i in line.split(' ')]]
    for i in range(len(line)-1):
        tab = fonc(tab)
        flag = False
        if tab[-1] == []:
            break
    
    res = 0
    #next
    for i in range(len(tab)-2, -1, -1):
        res = tab[i][-1] + res
        
    res2 = 0
    for i in range(len(tab)-2, -1, -1):
        res2 = tab[i][0] - res2
        
    #backward
    solution += res
    solution2 += res2
    
print(solution)
print(solution2)