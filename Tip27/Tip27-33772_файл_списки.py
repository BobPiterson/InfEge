# Набор данных состоит из нечётного количества пар натуральных чисел. 
# Необходимо выбрать из каждой пары ровно одно число так, чтобы чётность суммы выбранных чисел совпадала с чётностью большинства 
# выбранных чисел и при этом сумма выбранных чисел была как можно меньше. 
# Определите минимальную сумму, которую можно получить при таком выборе. 
# Гарантируется, что удовлетворяющий условиям выбор возможен
#
#

m = []
sort_first = []
with open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/Новый план/27-B.txt') as file:
    for line in file:
        str_of_file = line.split()
        # добавлять в конец списка: 
        m.append(str_of_file)

# из первой строки файла забираем значение n
n = int(m[0][0])
# удалим из списка первый элемент
m.pop(0)
    
# Преобразовать строковые в int, при этом вложенный список переделать в простой список
for i in range(n):
    if int(m[i][0]) < int(m[i][1]):
        mini = int(m[i][0])
        maxi = int(m[i][1])
    else:
        mini = int(m[i][1])
        maxi = int(m[i][0])
    m[i][0] = mini
    m[i][1] = maxi

lambda sorts: sorts[0]
sort_first = sorted(m, key=lambda sorts: sorts[0])
#print (sort_first)
#sort_second = sorted(m, key=lambda sorts: sorts[1])
#print(sort_second)

minsumma1 = 1e10
for k in range(n):
    summa = 0
    count_chet = 0
    for i in range(n):
        if i != k: 
            select = sort_first[i][0]
        else:
            select = sort_first[i][1]
        summa = summa + select
        # Подсчитаем количество четных чисел
        if select % 2 == 0: 
            count_chet += 1

    # if n / 2 < count_chet:
    #     print('Большинство выбранных чисел четные:', count_chet, '>', n // 2)
    # else:
    #     print('Большинство нечетные')
    # if summa % 2 == 0:
    #     print('Сумма выбранных чисел четная:', summa)
    # else:
    #     print('Сумма нечетная:', summa)
    if (n / 2 < count_chet) == (summa % 2 == 0):
        minsumma1 = min(minsumma1, summa)

print(minsumma1)
