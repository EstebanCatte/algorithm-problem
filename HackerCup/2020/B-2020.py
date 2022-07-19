def count(chaine):
    number_auburn = 0
    number_black = 0
    for s in range(len(chaine)):
        if chaine[s] == "A":
            number_auburn += 1
        if chaine[s] == "B":
            number_black += 1
    return number_auburn, number_black

def process(thefile):
    N = int(thefile.readline())
    seq = thefile.readline()
    number_auburn, number_black = count(seq)
    if abs(number_auburn-number_black) != 1:
        return "N"
    else:
        if N>=3:
            return "Y" 
        else:
            return "N" 

inputs = open("alchemy_input.txt", "r")
outputs = open("alchemy_outputs.txt", "w")
T = int(inputs.readline())

for t in range(T):
    outputs.write("Case #{}: {}".format(t,process(inputs)))
    outputs.write("\n")
