# Тип 9 № 64894
#Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
#Назовём ячейку таблицы интересной, если выполняются следующие условия:
#—  число в данной ячейке больше не встречается в данной строке;
#—  число в данной ячейке встречается в данном столбце, включая данную ячейку, больше 150 раз.
#Определите количество строк таблицы, содержащих не менее 5 интересных ячеек.

count = 0
file = open(r"D:\Downloads\09.txt").readlines()
#s = list(map(int, file[0].split()))
#print(s)
# создаем вложенный список столбцов
line = []

for i in file:
    s = list(map(int, i.split()))
    line.append(s)
#print(line)
#len(line)
col = [[0 for _ in range(len(line))] for _ in range(6)]
#print(col, len(line))

# Перегоним список строк(16000 строк * 6 элементов) в список столбцов (6 столбцов * 16000 элементов)
for i in range(len(line)):
    for j in range(6):
        #print(line[i][j])
        col[j][i] = line[i][j]
print('--------------------------', col[0][0], col[5][16000-1])

for i in range(len(line)):
    if len(line[i]) == len(set(line[i])): 
    #line[i].count(line[i][0]) == 1:
        count_interest = 0
        #print(line[i]) 
        if col[0].count(col[0][i]) > 150:
            count_interest += 1
        if col[1].count(col[1][i]) > 150:
            count_interest += 1
        if col[2].count(col[2][i]) > 150:
            count_interest += 1
        if col[3].count(col[3][i]) > 150:
            count_interest += 1
        if col[4].count(col[4][i]) > 150:
            count_interest += 1
        if col[5].count(col[5][i]) > 150:
            count_interest += 1
        if count_interest >= 5:
            count += 1
        # for j in range(6):
        #     #print(col[j][i])
        #     #print(col[j].count(col[j][i]))
        #     if col[j].count(col[j][i]) > 150:
                
print(count)
#Ответ: 9527.
