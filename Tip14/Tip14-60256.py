# https://inf-ege.sdamgia.ru/problem?id=60256
abc = '0123456789abcdefghi'
for i in abc:
    slag1 = int('98897' + i + '21', 19)
    slag2 = int('2' + i + '923', 19)
    if (slag1 + slag2) % 18 == 0:
        print(i, (slag1 + slag2) // 18)