lin = input()
lower_prop, upper_prop, under, symb = 0,0,0,0
for i in lin:
    if i.isupper():
        upper_prop+=1
    elif i.islower():
        lower_prop+=1
    elif i=="_":
        under+=1
    else:
        symb+=1
print(under/len(lin))
print(lower_prop/len(lin))
print(upper_prop/len(lin))
print(symb/len(lin))
