n = int(input())
a = 7
for i in range(n):
    inp = input()
    if inp=="Skru op!" and (a < 10):
        a += 1
    elif a>0:
        a -= 1
print(a)