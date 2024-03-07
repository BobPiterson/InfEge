import time
f = open("D:/Users/bobpi/Downloads/e2.txt").read().split()
n = f[0]
# Четвертая пара строк из файла
text = f[7]
fano = f[8]
#print(text)
print(len(text), len(fano))
abc = 'abcdefghij'

# statistics
# ------------------------------------------------------------------------------------------------------
# подсчет повторений каждого символа, в том числе подсчет количества повторений символов, стоящих подряд (до 10 подряд)
# stat = []
# includ = set()
# for c in text:
#     for i in range(1, 10):
#         if not (c * i in includ):
#             if text.count(c * i) != 0:
#                 stat.append([c * i, text.count(c * i)])
#                 includ.add(c * i)
# stat.sort()
# print(stat)

# подсчет повторений самых частых пар символов (ищем от 17 до 30 повторений)
# stat = []
# includ = set()
# for c in text:
#     for a1 in abc:
#         for a2 in abc:
#             for i in range(17, 30):
#                 tmp = a1 + a2
#                 if not (tmp in includ):
#                     if text.count(tmp) == i:
#                         stat.append([tmp, text.count(tmp)])
#                         includ.add(tmp)
#                         print(tmp, '=', text.count(tmp))

# stat.sort()
# print(stat)

# Подсчет количества повторяющихся ПОДРЯД кодов для повторяющихся подряд символов (repeat_char - количество повторов)
# repeat_char = 3
# exponent = 18
# for e in range(1, exponent):
#     for i in range(2 ** e):
#         #if i % 1000000 == 0: print(i)
#         subs = f"{i:0{e}b}"
#         if fano.count(subs * repeat_char) >= 2:
#             print('eee or jjj? =', (subs + ' ') * repeat_char, fano.count(subs * repeat_char))

# Подсчет количества повторения кодов (из разных символов) во всем списке кодов фано
# exponent = 20
# for e in range(1, exponent):        
#     for i in range(2 ** e):
#         subs = f"{i:0{e}b}"
#         if fano.count(subs) >= 17:
#             print('cc? =', subs, fano.count(subs))

# подсчет повторений самых длинных подстрок в тексте
# maxlen_2 = 0
# maxlen_3 = 0
# for i in range(len(text)):
#     sub = ''
#     for j in range(i, len(text)):
#         sub = sub + text[j]
#         if text.count(sub) == 2 and maxlen_2 < len(sub):
#             maxlen_2 = len(sub)
#             print('2 повтора', sub)
#         if text.count(sub) == 3 and maxlen_3 < len(sub):
#             maxlen_3 = len(sub)
#             print('3 повтора', sub)

# подсчет повторений самых длинных подстрок в фано (медленная)
# maxlen_2 = 0
# maxlen_3 = 0
# for i in range(len(fano)):
#     if i % 1000 == 0: print('step', i)
#     sub = ''
#     for j in range(i, len(fano)):
#         sub = sub + fano[j]
#         if len(sub) > len(fano) // 30:
#             break
#         if fano.count(sub) == 2 and maxlen_2 < len(sub):
#             maxlen_2 = len(sub)
#             maxstring2 = sub
#         if fano.count(sub) == 3 and maxlen_3 < len(sub):
#             maxlen_3 = len(sub)
#             maxstring3 = sub
# print('2 повтора', maxstring2)
# print('3 повтора', maxstring3)

# ----------------------------------------------------------------------------------------------------------------------
# найденные соответствия
# diction1 = [['a', '0011010000'], ['b', '1010111110'], ['c', '0100111100'], ['d', '1000010101'], ['e', '1000110010'], \
#            ['f', '0010101001'], ['g', '1111111010'], ['h', '0001111110'], ['i', '0001010100'], ['j', '1010100101']]

diction2 = [['a', '0000000001'], ['b', '0000000010'], ['c', '0000000011'], ['d', '0000000100'], ['e', '0000000101'], \
           ['f', '0000000110'], ['g', '0000000111'], ['h', '0000001000'], ['i', '0000001001'], ['j', '0000001010']]


# Замена кода фано на найденные соответствия и сохранение в список text2
subs = ''
text2 = ''
for s in fano:
    subs = subs + s
    for i in range(len(diction2)):
        if diction2[i][1] == subs:
            text2 = text2 + diction2[i][0]
            subs = ''
            break
print()
print(text2)
print()
if text2 == text:
    print('Все элементы совпадают, таблица найдена: ', diction2)
else:
    print('Полного соответствия нет')