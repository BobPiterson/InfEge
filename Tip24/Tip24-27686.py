# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности,
# состоящей из символов X.
# Хотя бы один символ X находится в последовательности.


count = 0
maxcount = 0
s = open(r"C:\Users\vngorlachev\Downloads\27686.txt").read()
for i in s:
    if i == 'X':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print('Ответ: ', maxcount)
# Ответ: 19