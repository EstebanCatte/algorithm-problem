width = int(input())
N = int(input())
area = 0
for i in range(N):
    x,y = input().split()
    area += int(x)*int(y)

print(int(area/width))