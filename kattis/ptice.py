N = int(input())
seq = input()
adrian = ['A','B','C']*100
bruno = ['B','A','B','C']*100
goran = ['C', 'C', 'A', 'A', 'B', 'B']*100
a,b,g = 0,0,0
for i in range(len(seq)):
    if seq[i] == adrian[i]: a+=1
    if seq[i] == bruno[i]: b+=1
    if seq[i] == goran[i]: g+=1

best = max([a,b,g])
print(best)
if a == best:
    print("Adrian")
if b == best:
    print("Bruno")
if g == best:
    print("Goran")

