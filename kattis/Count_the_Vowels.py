s = list(input().lower())
print(sum(s.count(v) for v in 'aeiou'))