f = open("C:/Users/vngorlachev/Downloads/26_17537.txt").readlines()
zan_place = f[0].split()[0]
row = f[0].split()[1]
place_in_row = f[0].split()[2]
print('Количество занятых мест', zan_place)
print('Количество рядов в зале', row)
print('Количество мест в каждом ряду', place_in_row)
# удалим первую строку из файла
f.pop(0)
# заведем список с номерами рядов и занятых мест
m = []
# заполним список списками из двух целых значений: номер ряда и номер занятого места
for i in range(len(f)):
    m.append([ int(f[i].split()[0]), int(f[i].split()[1]) ])

#print(m[-1])

