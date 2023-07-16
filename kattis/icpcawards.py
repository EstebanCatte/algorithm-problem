n = int(input())
winners = []
for _ in range(n):
    u,t = input().split()
    flag = True
    for i in range(len(winners)):
        if winners[i][0] == u:
            flag = False
    if flag and len(winners) < 12:
        winners.append([u,t])

for k in range(12):
    print(winners[k][0],winners[k][1])