# Сколько значащих нулей в двоичной записи числа
# 8 ** 820 - 2 ** 760 + 14
res10 = 8 ** 820 - 2 ** 760 + 14
res2 = bin(res10)[2:]
print(res2.count('0'))