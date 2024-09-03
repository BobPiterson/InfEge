x = 9 ** 8 + 3 ** 5 - 9
result = ''
while x > 0:
    result = str(x % 3) + result
    x = x // 3
print(result.count('2'))