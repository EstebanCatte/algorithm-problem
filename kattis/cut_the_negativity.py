a = [list(map(int, input().split())) for _ in range(int(input()))]
p = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] > 0: p.append((i+1, j+1, a[i][j]))
print(len(p))
for i, j, k in p: print(i, j, k)