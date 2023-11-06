n = int(input())
t = [int(i) for i in input().split()]
u = 0
for i in t:
    if i<0:
        u+=1
print(u)