import re
s = [input(), input()][1]
print(max(map(int, re.findall('\d+', s))))