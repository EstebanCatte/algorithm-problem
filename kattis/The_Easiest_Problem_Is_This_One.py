while True:
    number = int(input())
    if number == 0:
        break

    a = sum([int(i) for i in str(number)])
    p = 11
    while 1:
        b = sum([int(i) for i in str(number*p)])
        if a == b:
            print(p)
            break
        p+=1
