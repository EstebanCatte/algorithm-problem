s = input()
b = list(s)
b.sort()
a = 1
for j,i in enumerate(b[:-1]):
    if b[j] == b[j+1]:
        a = 0
        break
print(a)