# https://kompege.ru/variant
# вывести все числа меньше 1000 000 000, которые делятся на 8387 и имеют маску *75?122*
# также вывести результат деления каждого найденного числа на 8387
for i in range(0, 1000000000, 8387):
    s = str(i)
    if s[0:2] == '75' and s[3:6] == '122' or \
    s[1:3] == '75' and s[4:7] == '122' or \
    s[2:4] == '75' and s[5:8] == '122' or \
    s[3:5] == '75' and s[6:9] == '122':
        print(s, int(s) // 8387)