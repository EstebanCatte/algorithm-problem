def fonction(chaine, duplica='!'):
    """This function takes a string and add an extra character to each groups of <duplica> characters.
    Spaces are ignored and do not separates groups.
    Complexity : O(n)

    Args:
        chaine (String): String to process
        duplica (Char): Charactere to duplicate. Defaults to '!'.

    Returns:
        String: Transformated new string
    """
    anwser = ""
    temp = ""
    flag = 1
    
    for i in range(len(chaine) - 1, -1, -1):
        carac = chaine[i]
        
        if carac != duplica:
            temp = carac + temp
            if carac != ' ': flag = 0
        else:
            temp = duplica + temp
            if not flag:
                anwser = temp[1:]+ duplica*(temp[-1]==duplica) + anwser
                temp = duplica
                flag = 1
    
    if temp == duplica : flag = 0
    anwser = temp + duplica*(not flag) + anwser
    return anwser

# Exemple
chaine = "Hello! !!o o! !world"
resultat = fonction(chaine, duplica='d')
print(resultat)