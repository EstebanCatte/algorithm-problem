inp = str(input()).split(";")

compt = 0
for i in inp:
    if "-" in i:
        temp = i.split("-")
        compt = compt+ int(float(temp[1])) - int(float(temp[0])) + 1
    else:
        compt += 1

print(compt)