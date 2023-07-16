import math
h,v = input().split()
h,v = int(h), int(v)
print(math.ceil(h/math.sin(v*math.pi / 180)))