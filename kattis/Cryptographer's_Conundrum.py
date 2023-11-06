text = input()
sum = 0
a = ['P','E','R']*300
for i in range(len(text)):
    if text[i] != a[i]:
        sum+=1
print(sum)