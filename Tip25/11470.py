def divisors_cnt(x):
    cnt = 2
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            cnt += 1
            if i != x // i:
                cnt += 1

    return cnt


def find_first_primes(n):
    l = []
    for i in range(2, n):
        if divisors_cnt(i) == 2:
            l.append(i)

    return l


def find_prime_divisors(x, primes):
    l = dict()
    i = 0
    while x != 1:
        if x % primes[i] == 0:
            if primes[i] not in l:
                l[primes[i]] = 1
            else:
                l[primes[i]] += 1
            x //= primes[i]
        else:
            i += 1

    return l


m = 0
# primes = find_first_primes(1000)
# for i in range(1, 100000):
#     cnt = divisors_cnt(i)
#     if cnt > m:
#         m = cnt
#         print(i, m, find_prime_divisors(i, primes))

print(divisors_cnt(97772875200), divisors_cnt(97772875200 / 2))
