import time
f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/e2.txt").read().split()
n = f[0]
text = f[1]
fano = f[2]
print(len(text), len(fano))
abc = 'abcdefghij'

# statistic
# ------------------------------------------------------------------------------------------------------
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

# подсчет повторений самых частых пар символов
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
# stat.sort()
# print(stat)

# Подсчет количества повторяющихся кодов в списке кодов фано
# for i in range(2 ** 12, 2 ** 20):
#     subs = bin(i)[2:]
# #    if fano.count(subs * 6) == 1:
#     if fano.count(subs) == 18:
#         print('bh, he =', subs, fano.count(subs))
#     # if fano.count(subs * 4) == 1:
#     #     print('h =', subs, fano.count(subs))

# print(text.count('bhe'))

# найденные соответствия
diction1 = [['a', '0011010000'], ['b', '1010111110'], ['c', '0100111100'], ['d', '1000010101'], ['e', '1000110010'], \
           ['f', '0010101001'], ['g', '1111111010'], ['h', '0001111110'], ['i', '0001010100'], ['j', '1010100101']]

# Замена кода фано на найденные соответствия и сохранение в список text2
subs = ''
text2 = ''
for s in fano:
    subs = subs + s
    for i in range(len(diction1)):
        if diction1[i][1] == subs:
            #print(diction[i][0], end='')
            text2 = text2 + diction1[i][0]
            subs = ''
            break
        else:
            text2 = text2 + ''
print()
print(text2)
print()
if text2 == text:
    print('Все элементы совпадают, таблица найдена: ', diction1)