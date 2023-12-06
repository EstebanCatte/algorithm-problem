n = int(input())
sum = 0
for i in range(n):
    a = input()
    sum += int(a[:-1])**int(a[-1])
print(sum)