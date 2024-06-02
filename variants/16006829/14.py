v = 4 ** 255 + 2 ** 255 - 255

cnt = bin(v)[2:].count('1')
print(cnt)