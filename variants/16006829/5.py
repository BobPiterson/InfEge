for N in range(0, 256):
    x = '0' * (8 - len(bin(N)[2:])) + bin(N)[2:]
    x = ''.join((map(lambda x1: '0' if x1 == '1' else '1', x)))
    R = int(x, 2)
    R = R - N
    if R == 133:
        print(N)
        break
        