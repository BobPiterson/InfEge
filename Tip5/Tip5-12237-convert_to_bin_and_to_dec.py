# Поиск минимального R удовлетворяющего требованиям
def step(n2):
    if n2[-1:] == '0':
        n2 = n2 + n2[-2:]
    else:
        n2 = '1' + n2 + '0'
    return n2

n10max = 0
for n10 in range(1,1000):
    n2 = bin(n10)[2:]
    r = int(step(n2), 2)
    if r < 100:
        n10max = n10

print(n10max, int(step(bin(n10max)[2:]), 2))


