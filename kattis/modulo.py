dic = {}
for i in range(10):
    n = int(input())
    dic[n%42] = 1
print(len(dic))
