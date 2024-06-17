# def divs(x):
#     cnt = 0
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             if i % 2 != 0:
#                 cnt += 1
#             if i != x // i and x // i % 2 != 0:
#                 cnt += 1
#
#     return cnt
#
#
# for i in range(45_000_000, 50_000_001):
#     if divs(i) == 5:
#         print(i)


def divs2(x):
    if x == 1:
        return False
    if x == 2:
        return True

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


for i in range(45_000_000, 50_000_001):
    x = i
    while x % 2 == 0:
        x //= 2

    if int(int(x ** 0.25) ** 4) == x and divs2(int(x ** 0.25)):
        print(i)
