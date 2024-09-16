# Программа, которая принимает текст из файла и выводит два слова: 
# 1) наиболее часто встречающееся, длиннее 10 букв
# 2) самое длинное слово

f = open("D:/Documents/репетиторство/15.Материалы ЕГЭ/Новые материалы/Большой_текстовый_файл.txt").read()
lst = f.split()
#print(lst[0], lst[1], lst[5], lst[10])
maxlen = 0
maxlenword = ''
word = ''
count = 0
for s in lst:
    if len(s) > maxlen:
        maxlen = len(s)
        maxlenword = s
    if len(s) > 10:
        tmp = lst.count(s)
        if tmp > count:
            word = s
            count = tmp

    
print('Самое часто встречающееся слово длиннее 10 букв и количество его повторений: ', word, count)
print('Самое длинное слово и его длина: ', maxlenword, maxlen)

