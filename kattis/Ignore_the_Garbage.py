def f(n):
    #(0,1,2,3,4,5,6) to (0,1,2,5,6,8,9) then to (0,1,2,5,9,8,6)
    temp = n
    x = 0
    if n==0:
        print(0,end='')
    else:
        while (temp>0):
            x = temp%7
            temp = temp//7
            if (x == 3): print(5, end='')
            elif (x == 4): print(9, end='')
            elif (x == 5): print(8, end='')
            else: print(x, end='')
    print("")

while(True):
    n = int(input())
    f(n)
