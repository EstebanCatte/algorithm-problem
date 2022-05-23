
def generate_array(N,C):
    mini, maxi = N-1, sum(range(2, N+1))
    if C < mini or C > maxi:
        return 'IMPOSSIBLE'

    pos = list(range(N))
    cost = [1]* (N-1)
    C = C - N +1 #retire le minimum pour voir ce qu'il reste à faire
    i = 0
    while i<N-1: #parcours les pos
        cur = min(C, N-i-1)
        cost[i] += cur
        pos[i: i+cost[i]] = reversed(pos[i: i+cost[i]])
        C -= cur
        i +=  1
    res = [0]*N
    for num, i in zip(range(1, N+1), pos):
        res[i] = num
    return ' '.join(map(str, res))
    
if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N, C = input().split()
        N, C = int(N), int(C)
        print("Case #{}:".format(t), generate_array(N, C)) 