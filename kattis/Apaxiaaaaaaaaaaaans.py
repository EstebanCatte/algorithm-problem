n = input()
anwser = ""+n[0]
for i in range(1,len(n)):
    if n[i-1] != n[i]:
        anwser+=n[i]
print(anwser)
