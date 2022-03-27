carac = str(input())
res = ""
for c in carac:
    if ord(c) > 64 and ord(c)<91:
        res = res+c
print(res)