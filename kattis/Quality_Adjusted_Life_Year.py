n = int(input())
sum = 0
for i in range(n):
    line = input()
    q, t = line.split()
    sum += float(q)*float(t)
print(sum)