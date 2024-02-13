# https://kompege.ru/variant
# Аня составляет трехзначные числа в десятичной системе счисления,
# в которых цифры расположены в порядке неубывания.
# Сколько различных чисел может составить Аня?
count = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a <= b and b <= c:
                count += 1
                print(a,b,c)
print(count)
