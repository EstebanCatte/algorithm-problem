N = int(input())
if N%2==1:
    print("still running")
else:
    s = 0
    temp = 0
    for i in range(N):
        inp = int(input())
        if i%2 == 0:
            temp = inp
        else:
            s = s + (inp - temp)

    print(s)