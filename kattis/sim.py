from collections import deque

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

T = int(float(input()))
for i in range(T):
    string = input()
    cursor = 0
    res = deque()
    for charac in string:
        #print("process charac {}".format(charac))
        if charac == "[":
            cursor = 0
            continue
        if charac == "<" and cursor > 0:
            cursor -= 1
            delete_nth(res, cursor)
            continue
        if charac == "]":
            cursor = len(res)
            continue
        if cursor == len(res):
            res.append(charac)
            cursor += 1
        else:
            res.insert(cursor, charac)
            cursor += 1
        #print("res = {}".format(res))
    print(''.join(res))
