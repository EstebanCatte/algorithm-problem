n = int(input())
line = [int(i) for i in input().split()]
line2 = [int(i) for i in input().split()]
print([i for i in line if i not in line2][0])