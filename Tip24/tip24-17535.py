# Текстовый файл состоит из символов A, B, C, D, E, F.
# Определите максимальное количество идущих подряд символов в файле,
# среди которых пара символов CD (в указанном порядке) встречается ровно 160 раз.

f = open("C:/Users/vngorlachev/Downloads/24_17535.txt").readline()
n = [] #создаем пустой массив для индексов букв CD
m = 0 # пол для максимума
# ищем пары CD и их индексы (индекс начала пары, символа C) добавляем в n
for i in range(len(f) - 1):
    if f[i] == 'C' and f[i+1] == 'D':
        n.append(i)

#print(n[0], n[1], n[2], n[3], len(n))
# в массиве с индексами проверяем все отрезки подпоследовательности длиной 160 пар CD
for i in range (len(n)- 161):
    m = max(m, n[i + 161] - n[i]) # 161 получается так как надо учесть две буквы: CD

print (m)