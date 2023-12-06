a = input()
ff = False
for i in range(1, len(a)):
    if(a[i]=='s' and a[i-1] == 's'):
        ff = True
        break
if not ff:
    print("no hiss")
else:
    print("hiss")