
r = '1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine'.split()
f = lambda s, d: min((s[::d].find(l[::d])%99, i) for i, l in enumerate(r))[1]
print(sum(f(x, 1) % 9 * 10 + f(x, -1) % 9 + 11 for x in open('C:/Users/Esteban/Documents/GitHub/algorithm-problem/adventofcode2023/input1')))