# https://inf-ege.sdamgia.ru/problem?id=60267
for i in range(0, 10000000000, 2024):
    s = str(i)
    if s[0:1] == '1' and s[2:5] == '2157' and s[6:0] == '4' or \
    s[0:1] == '1' and s[2:5] == '2157' and s[7:0] == '4' or \
    s[0:1] == '1' and s[2:5] == '2157' and s[8:0] == '4' or \
    s[0:1] == '1' and s[2:5] == '2157' and s[9:0] == '4' or \
    s[0:1] == '1' and s[2:5] == '2157' and s[10:0] == '4':
        print(s, int(s) // 2024)