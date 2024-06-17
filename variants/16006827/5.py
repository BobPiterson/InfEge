s = set()
for N in range(10, 1001):
    R = N - int(bin(N)[3:], 2)
    s.add(R)

print(len(s))


