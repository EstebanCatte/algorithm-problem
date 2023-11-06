n = int(input())
for i in range(n):
    r,e,c = input().split()
    r,e,c = int(r), int(e), int(c)
    if e - c > r : print("advertise")
    if e - c == r : print("does not matter")
    if e - c < r : print("do not advertise")


