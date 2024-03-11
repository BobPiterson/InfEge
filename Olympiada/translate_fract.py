from string import digits, ascii_lowercase

alp = digits + ascii_lowercase


def translate_int(num, base):
    s = ''
    while num:
        s += alp[num % base]
        num //= base
    return s[::-1] if s else '0'


def translate_float(num, div, base, length=10000):
    s = ''
    while num and len(s) < length:
        s += alp[num * base // div]
        num = num * base % div
    return s if s else '0'


def translate(num, div, base, length=10000):
    return f'{translate_int(num // div, base)}.{translate_float(num % div, div, base, length)}'


if __name__ == '__main__':
    print(translate(125, 351, 9))
    print(125 / 351)
    print(int('31754', 9) / 9 ** 5)

# Z;10 = 0.31(754);9

# 0.00(754);9 = M;10 | * 100
# 0.(754) = 81M| * 100
# 0.(754) = 81M| * 1000
# 754.(754) = 59049M| - 81M
# 754;9 = 58968M;
# M = 616 / 58968
# M = 11 / 1053

# 0.31;9 = X;10 | * 100
# 31;9 = 81X
# X = 28 / 81

# Z = X + M
# Z = 28 / 81 + 11 / 1053
# Z = 364 / 1053 + 11 / 1053
# Z = 375 / 1053
# Z = 125 / 351
