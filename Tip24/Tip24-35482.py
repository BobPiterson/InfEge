# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв G
# (если таких строк несколько, надо взять ту, которая находится в файле раньше), и определить,
# какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
#
m =  open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/24 (1).txt').readlines()
# Найдем номер первой строки, в которой реже всего встречается символ 'G'
mincount = 1000000
for i in range(len(m)):
    if m[i].count('G') < mincount:
        mincount = m[i].count('G')
        numberstring = i
#print(numberstring, mincount)
# Создадим пустой словарь со всеми заглавными буквами латинского алфавита
ABC_dict = {chr(a): 0 for a in range(ord("A"), ord("Z")+1)}
# в конце строки стоит символ перевода строки '\n', уберем его:
m[numberstring] = m[numberstring][:-1]
# Посчитаем количество появлений каждого символа в найденной строке:
for c in m[numberstring]:
    ABC_dict[c] = ABC_dict[c] + 1
#print(ABC_dict)
# Найдем повторяющийся чаще всего символ (последний, если таких несколько):
maxRepeatChar = 0
for i in ABC_dict:
    if ABC_dict[i] >= maxRepeatChar:
        maxRepeatChar = ABC_dict[i]
        maxChar = i
print(maxChar)
