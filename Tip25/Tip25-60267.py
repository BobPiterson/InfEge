# https://inf-ege.sdamgia.ru/problem?id=60267
# 1?2157*4, делящиеся на 2024 без остатка
for i in range(0, 10000000000, 2024):
    s = str(i)
    if s[0:1] == '1' and s[2:6] == '2157' and s[6:7] == '4' and s[7:] == '' or \
    s[0:1] == '1' and s[2:6] == '2157' and s[7:8] == '4' and s[8:] == '' or \
    s[0:1] == '1' and s[2:6] == '2157' and s[8:9] == '4' and s[9:] == '' or \
    s[0:1] == '1' and s[2:6] == '2157' and s[9:10] == '4' and s[10:] == '' or \
    s[0:1] == '1' and s[2:6] == '2157' and s[10:11] == '4' and s[11:] == '' :
        print(s, int(s) // 2024)