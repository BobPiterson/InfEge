def b(x):
    return '0' * (8 - len(bin(x)[2:])) + bin(x)[2:]

print(b(224))
print(157 & 224)
print(157 - 128)