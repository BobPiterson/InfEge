v = 49 ** 8 + 7 ** 24 - 7

s = ''
while v:
    s += str(v % 7)
    v //= 7

print(s.count('0'))
