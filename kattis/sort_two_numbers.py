line = input()
a, b = line.split()
a = int(a)
b = int(b)
if b < a:
    print("{} {}".format(b, a))
else:
    print("{} {}".format(a ,b))