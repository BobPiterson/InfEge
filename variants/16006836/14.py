v = 2 * 216 ** 8 + 4 * 36 ** 12 + 6 ** 15 - 1296

s = ''
while v:
    s += str(v % 6)
    v //= 6

s = s[::-1]
print(s.count('0'))

