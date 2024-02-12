# 56533

def do(x) -> int:
    for i in range(3):
        s = sum(ord(j) - ord('0') for j in str(x))

        if s % 2 != 0:
            x = x * 2 + 1
        else:
            x = x * 2

    return x


def interval(x) -> bool:
    return 987654321 <= x <= 2123456789


n = 987654321 // 8
l = 0
for i in range(n - 1000, n + 1000):
    if interval(do(i)):
        l = i
        break

n = 2123456789 // 8
r = 0
for i in range(n + 1000, n - 1000, -1):
    if interval(do(i)):
        r = i
        break

print(r - l + 1)
