from math import log


def f(n):
    # print(n)
    if n < 9:
        return n

    return f(n % 9) + f(n // 9)


v1 = '8' * 15 + "00"
print(int(v1, 9))
print(v1)

v = 4 * 6 ** 20
v0 = v
print(f(v))
s = ''
while v:
    s += str(v % 9)
    v //= 9
s = s[::-1]
print(s)

v = 5 * 6 ** 20
v2 = v
print(f(v))
s = ''
while v:
    s += str(v % 9)
    v //= 9
s = s[::-1]
print(s)

print(v0, int(v1, 9), v2)
# cnt = 0
# for i in range(4 * 6 ** 20, 5 * 6 ** 20 + 1):
#     if f(i) == 121:
#
#         cnt += 1

# print(cnt)
