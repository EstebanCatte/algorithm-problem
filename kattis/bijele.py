liste = [int(i) for i in input().split()]
u = [1,1,2,2,2,8]
for i, piece in enumerate(liste):
    print(u[i] - piece, end=" ")
