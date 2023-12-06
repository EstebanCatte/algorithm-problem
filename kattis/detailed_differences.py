n = int(input())

for i in range(n):
    line1 = input()
    line2 = input()
    res = []
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            res.append('.')
        else:
            res.append('*')

    print(line1)
    print(line2)
    print(''.join(res))
    print("")