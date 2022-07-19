import numpy as np

T = int(input())
for t in range(T):
    print('Case #{}:'.format(t))
    N = int(input())
    result = []
    ii = input()
    oi = input()
    left, right = -1, -1
    for current in range(N):
        if not (current-1 >=0 and oi[current] == ii[current-1] == 'Y'):
            left = current
            print("left= {}".format(current))
        if right < current:
            right = current
            print("right= {}".format(current))
            while right+1 < N and oi[right] == ii[right+1] == 'Y':
                right+=1 #path is ok
                print("right+1")
        result = 'N'*left + 'Y'*(right-left-1) + 'N'*(N-1-right)
        print(result)
