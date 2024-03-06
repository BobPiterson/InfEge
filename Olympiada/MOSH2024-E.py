import time
f = open("C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/txt/e2.txt").read().split()
n = f[0]
#print(n)
text = f[1]
fano = f[2]
#print(f[1][-1])
print(len(text), len(fano))

# statistic
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

abc = 'abcdefghij'

# stat = []
# includ = set()
# for c in text:
#     for a1 in abc:
#         for a2 in abc:
#             for i in range(18, 30):
#                 tmp = a1 + a2
#                 if not (tmp in includ):
#                     if text.count(tmp) == i:
#                         stat.append([tmp, text.count(tmp)])
#                         includ.add(tmp)
# stat.sort()
# print(stat)


# for i in range(2 ** 12, 2 ** 20):
#     subs = bin(i)[2:]
# #    if fano.count(subs * 6) == 1:
#     if fano.count(subs) == 18:
#         print('bh, he =', subs, fano.count(subs))
#     # if fano.count(subs * 4) == 1:
#     #     print('h =', subs, fano.count(subs))

# print(text.count('bhe'))
# print(fano.count(''))
abc = 'abcdefghij'
diction = [['a', '.'], ['b', '1010111110'], ['c', '.'], ['d', '1000010101'], ['e', '.'], \
           ['f', '0010101001'], ['g', '1111111010'], ['h', '0001111110'], ['i', '0001010100'], ['j', '.']]


fano = fano.replace(diction[8][1], 'i')
fano = fano.replace(diction[6][1], 'g')
fano = fano.replace(diction[1][1], 'b')
    #print(diction[i][1], diction[i][0], fano)
    #time.sleep(10)
print(fano)

# subs = ''
# text2 = ''
# for s in fano:
#     subs = subs + s
#     #print(subs)
#     #time.sleep(0.01)
#     for i in range(len(diction)):
#         #print(diction[i][1])
#         if diction[i][1] == subs:
#             print(diction[i][0], end='')
#             text2 = text2 + diction[i][0]
#             subs = ''
#             break
#         else:
#             text2 = text2 + ''
# print()
# print(text2)


# subs = ''
# for s in fano:
#     subs = subs + s
#     print(subs, fano.count(subs))
#     time.sleep(5)
#     if fano.count(subs) == 101:
#         print(subs)