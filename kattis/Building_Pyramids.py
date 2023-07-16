n = int(input())

h = 1
while h*(2*h-1)*(2*h+1) <= 3*n:
    h += 1
print(h-1)