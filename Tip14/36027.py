v = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255

s = ''
while v:
    s += str(v % 8)
    v //= 8

print(s.count('0'))

