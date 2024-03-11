import time
f = open("D:/Users/bobpi/Downloads/e2.txt").read().split()
n = f[0]
# Седьмая пара строк из файла
text = f[13]
fano = f[14]
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
#             for i in range(14, 30):
#                 tmp = a1 + a2
#                 if not (tmp in includ):
#                     if text.count(tmp) == i:
#                         stat.append([tmp, text.count(tmp)])
#                         includ.add(tmp)
#                         print(tmp, '=', text.count(tmp))
# print(stat)

# Подсчет количества повторяющихся ПОДРЯД кодов для повторяющихся подряд символов (repeat_char - количество повторов)
# repeat_char = 3
# exponent = 18
# for e in range(1, exponent):
#     for i in range(2 ** e):
#         #if i % 1000000 == 0: print(i)
#         subs = f"{i:0{e}b}"
#         if fano.count(subs * repeat_char) >= 3:
#             print('eee? =', (subs + ' ') * repeat_char, fano.count(subs * repeat_char))

# Подсчет количества повторения кодов (из разных символов) во всем списке кодов фано
# exponent = 22
# for e in range(1, exponent):        
#     for i in range(2**10, 2 ** e):
#         subs = f"{i:0{e}b}"
#         if fano.count(subs) >= 14:
#             print('jg? =', subs, fano.count(subs))

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
diction2 = [['a', '0'], ['b', '10100'], ['c', '1001'], ['d', '101100001'], ['e', '100'], \
           ['f', '1111'], ['g', '1101'], ['h', '1110000'], ['i', '110011'], ['j', '110111']]


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