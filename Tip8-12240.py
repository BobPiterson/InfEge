# Сколько существует девятиричных пятизначных чисел, содержащих
# в своей записи ровно одну цифру 5, в которых никакие
# две одинаковые цифры не стоят рядом?

# Командой print(int('88888',9)) получим максимальное пятизначное девятиричное число, преобразованное в десятичное = 59048
# Командой print(int('10000',9)) получим минимальное пятизначное девятиричное число, преобразованное в десятичное = 6561
def s10_to_s9(n10):
    ost = ''
    while n10 > 0:
        ost = str(n10 % 9) + ost
        n10 = n10 // 9
    return ost

#print(int('10000',9))
count = 0
for n10 in range(6561, 59049):
    n9 = s10_to_s9(n10)
    if n9.count('5') == 1 and n9[0] != n9[1] and n9[1] != n9[2] and n9[2] != n9[3] and n9[3] != n9[4]:
        count += 1
    #if n10 % 6561 == 0: print(n9)
print('Ответ = ', count)
