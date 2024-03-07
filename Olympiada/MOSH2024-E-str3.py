import time
f = open("D:/Users/bobpi/Downloads/e2.txt").read().split()
n = f[0]
# Вторая строка из файла
text = f[3]
fano = f[4]
#print(text)
print(len(text), len(fano))
abc = 'abcdefghij'

# statistics
# ------------------------------------------------------------------------------------------------------
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


# подсчет повторений каждого символа, в том числе подсчет количества повторений символов, стоящих подряд
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
stat = []
includ = set()
for c in text:
    for a1 in abc:
        for a2 in abc:
            for i in range(17, 30):
                tmp = a1 + a2
                if not (tmp in includ):
                    if text.count(tmp) == i:
                        stat.append([tmp, text.count(tmp)])
                        includ.add(tmp)
                        print(tmp, '=', text.count(tmp))



# stat.sort()
# print(stat)

# Подсчет количества повторяющихся ПОДРЯД кодов для повторяющихся подряд символов (repeat_char - количество повторов)
# repeat_char = 3
# for i in range(2 ** 19):
#     subs = bin(i)[2:]
#     subs = subs[::-1]
#     if fano.count(subs * repeat_char) >= 2:
#         print('e, j =', subs * repeat_char, fano.count(subs * repeat_char))

# Подсчет количества повторения кодов (из разных символов) во всем списке кодов фано
# for i in range(2 ** 19):
#     subs = bin(i)[2:]
#     subs = subs[::-1]
#     if fano.count(subs) >= 16:
#         print('cb? =', subs, fano.count(subs))



# ----------------------------------------------------------------------------------------------------------------------
# найденные соответствия
# diction1 = [['a', '0011010000'], ['b', '1010111110'], ['c', '0100111100'], ['d', '1000010101'], ['e', '1000110010'], \
#            ['f', '0010101001'], ['g', '1111111010'], ['h', '0001111110'], ['i', '0001010100'], ['j', '1010100101']]

diction2 = [['a', '1'], ['b', '01'], ['c', '001'], ['d', '0001'], ['e', '00001'], \
           ['f', '000001'], ['g', '0000001'], ['h', '00000001'], ['i', '000000001'], ['j', '0000000001']]


# Замена кода фано на найденные соответствия и сохранение в список text2
# subs = ''
# text2 = ''
# for s in fano:
#     subs = subs + s
#     for i in range(len(diction2)):
#         if diction2[i][1] == subs:
#             text2 = text2 + diction2[i][0]
#             subs = ''
#             break
# # print()
# # print(text2)
# print()
# if text2 == text:
#     print('Все элементы совпадают, таблица найдена: ', diction2)
# else:
#     print('Полного соответствия нет')