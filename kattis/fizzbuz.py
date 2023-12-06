X, Y, N = input().split()
for i in range(1, int(N)+1):
    if(i%int(X) == 0):
        if(i%int(Y) == 0):
            print("Fizzbuzz")
        else:
            print("Fizz")
    else:
        if(i%int(Y) == 0):
            print("Buzz")
        else:
            print(i)