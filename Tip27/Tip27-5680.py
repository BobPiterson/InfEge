# https://kompege.ru/variant
# Задача В выполняется 2,7 часа

f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/27B_5680.txt").read().split()
colvo = f[0]
minim = int(f[1])
large = int(f[2])
print(colvo, minim, large)
f.pop(0)
f.pop(0)
f.pop(0)
#print(f)
# подсчет суммы медленным алгоритмом
def summa(f: list, first: int) -> int:
    s = 0
    len_f = len(f)
    # подсчет суммы на участке M-L
    for j in range(minim, large + 1):
        point = first + j
        if point >= len_f:
            point -= len_f
        s += int(f[point]) * j
    return s

min_res = 1e9
for i in range(len(f)):
    if i % 1000 == 0: print('iteration = ', i, 'из', colvo)
    s = summa(f, i)
    if s < min_res:
        min_res = s

print(min_res)
