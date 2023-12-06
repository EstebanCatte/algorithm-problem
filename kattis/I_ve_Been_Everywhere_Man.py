n = int(input())
for i in range(n):
    t = int(input())
    a = {}
    for j in range(t):
        a[input()] = 1
    print(len(a.keys()))
