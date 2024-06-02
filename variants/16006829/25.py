def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

idx = 0
for i in range(245690, 245756 + 1):
    idx += 1
    if is_prime(i):
        print(idx, i)