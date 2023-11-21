n = int(input())
a = [[]]*n
for n in range(n):
    a[n] = [int(i) for i in input().split()]

print(a)
res = []
for i in range(len(a[0])):
    for j in range(n):
        if a[i][j] >= 0:
            i = str(i)+" "+str(j)+" "+str(a[i][j])
            res.append(i)

print(len(res))
for i in res:
    print(i)