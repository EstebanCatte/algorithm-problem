G, T, N = input().split()
a = input().split()
a = sum([int(i) for i in a])
print(int(0.9*(int(G) - int(T)) - a ))

