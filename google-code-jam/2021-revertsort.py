def reversort(n, L):
    cost = 0
    for i in range(n-1):
        minimum = min(L[i:])
        j = L.index(minimum) + 1
        L[i:j] = reversed(L[i: j])
        cost += j - i
    return cost

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        arr = list(map(int, input().split()))
        print("Case #{}:".format(t), reversort(N, arr))
