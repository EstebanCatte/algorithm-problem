def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

notes1 = sum([int(i) for i in input().split()])
notes2 = sum([int(i) for i in input().split()])
notes3 = sum([int(i) for i in input().split()])
notes4 = sum([int(i) for i in input().split()])
notes5 = sum([int(i) for i in input().split()])
a = [notes1, notes2, notes3, notes4, notes5]
print(str(argmax(a)+1)+" "+str(max(a)))