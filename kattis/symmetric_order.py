num = 1
y = 0
while num!=0:
    num = int(input())

    if num != 0:
        y+=1
        
        strs = []
        for i in range(num):
            strs.append(input())
        res = strs.copy()
        ptr = 0
        for a,i in enumerate(strs):
            if a%2==0:
                res[ptr] = i
            else:
                res[-(ptr+1)] = i
                ptr+=1

        print("SET {}".format(y))
        for i in res:
            print(i)


