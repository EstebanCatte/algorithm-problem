def append_sort():
    N = input()
    X = list(map(int, input().strip().split()))
    result = 0
    for i in range(1, len(X)):
        count = 0
        while X[i] <= X[i-1]:
            X[i] *= 10
            count += 1
        if count > 1 and (X[i]//10) + (10**(count-1)-1) > X[i-1]:
            X[i] = X[i-1]+1
            cnt -= 1
        result += count
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, append_sort()))