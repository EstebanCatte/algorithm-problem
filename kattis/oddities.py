n = int(input())

for i in range(n):
    a = int(input())
    if a%2==0:
        print("{} is even".format(a))
    else:
        print("{} is odd".format(a))