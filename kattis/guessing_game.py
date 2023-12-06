ptrr, ptrl, index = 10,1,0
number = 10
possible = "Stan may be honest"

while number != 0:
    number = int(input())

    if number != 0:
        instruction = input()
        if instruction == "right on":
            if number < ptrl or number > ptrr:
                print("Stan is dishonest")
            else:
                print("Stan may be honest")
            ptrr, ptrl = 10, 1

        if instruction == "too low" and number >= ptrl:
            ptrl = number+1

        if instruction == "too high" and number <= ptrr:
            ptrr = number-1