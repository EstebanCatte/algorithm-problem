n = int(input())
m = list(zip(*[list(map(int, input().split())) for _ in range(3)]))
print(*[sorted(x)[1] for x in m])