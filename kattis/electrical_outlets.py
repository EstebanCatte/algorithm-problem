N = int(input())
for i in range(N):
    line = [int(i) for i in input().split()]
    sum = 0
    for i in range(1,len(line)-1):
        sum += line[i]-1
    sum += line[-1]
    print(sum)
