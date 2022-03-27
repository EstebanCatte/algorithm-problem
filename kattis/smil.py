string = str(input())


for i, charac in enumerate(string):
    if i < len(string) - 1:
        if charac == ":" and string[i+1] == ")":
            print(i)
        if charac == ";" and string[i+1] == ")":
            print(i)
    if i < len(string) - 2:
        if charac == ":" and string[i+1] == "-" and string[i+2] == ")":
            print(i)
        if charac == ";" and string[i+1] == "-" and string[i+2] == ")":
            print(i)