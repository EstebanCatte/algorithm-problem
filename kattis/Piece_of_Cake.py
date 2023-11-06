n,h,v = input().split()
n,h,v = int(n), int(h), int(v)
print((max(n-h, h)*max(n-v, v))*4)
