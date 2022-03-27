N = int(float(input()))
M = int(float(input()))

reste = M%N
for i in range(N):
    if reste > 0:
        print("*"*((M//N)+1))
    else:
        print("*"*(M//N))
    reste -= 1