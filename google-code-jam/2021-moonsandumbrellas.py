# import sys

# def resolve(thestring):
#     global X
#     global Y

#     #Condition d'arret de la recursivité
#     if len(thestring) <= 1:
#         return 0 #une lettre seule ne coute rien
#     else:
#         C_string = thestring.copy() #used to replace by a C
#         J_string = thestring.copy() #used to replace by a J

#         #Case of chosing the minimum cost
#         if thestring[0] == "?":
#             C_string[0] = "C"
#             J_string[0] = "J"
#             return min(resolve(C_string), resolve(J_string))
        
#         else:
#             if thestring[0] == thestring[1]:
#                 #Continue
#                 return resolve(thestring[1:])
#             else:
#                 if thestring[0] == "C" and thestring[1] == "J":
#                     return X + resolve(thestring[1:])
#                 if thestring[0] == "J" and thestring[1] == "C":
#                     return Y + resolve(thestring[1:])
#                 if thestring[1] == "?":
#                     C_string[1] = "C"
#                     J_string[1] = "J"
#                     return min(resolve(C_string), resolve(J_string))




# if __name__ == "__main__":
#   sys.setrecursionlimit(10**6)
#   testcase = int(input())
#   for test in range(1, testcase+1):
#     X, Y, mystring = input().split()
#     X = int(X) #Cost for CJ
#     Y = int(Y) #Cost for JC

#     print("Case #" + str(test) + ": " + str( resolve( list(mystring) )) )


def moons_and_umbrellas():
    X, Y, S = input().split()
    X, Y = int(X), int(Y)
    dp = {}
    prev = None
    for c in S:
        new_dp = {}
        for i, j, cost in [('C', 'J', Y), ('J', 'C', X)]:
            if c == j:
                new_dp[i] = INF
            elif prev is None:
                new_dp[i] = 0
            elif prev == i:
                new_dp[i] = dp[i]
            elif prev == j:
                new_dp[i] = dp[j]+cost
            elif prev == '?':
                new_dp[i] = min(dp[i], dp[j]+cost)
        dp = new_dp
        prev = c
    return min(dp.values())

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, moons_and_umbrellas()))