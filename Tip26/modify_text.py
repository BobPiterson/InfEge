# Программа разбивает текстовый файл на строки длины lenString
# для вставки в шапку исходника

f = open(r"C:\Users\vngorlachev\Downloads\zad.txt", encoding='utf-8').readlines()
m = []
lenString = 75 # Удобная длина строки в символах
#print(f[0].split()[0:20])
for s in f:
    newString = '# '
    for w in s.split():
        if len(newString) + len(w) < lenString:
            newString += (w + ' ')
        else:
            m.append(newString)
            newString = '# ' + w + ' '
    m.append(newString)

with open(r"C:\Users\vngorlachev\Downloads\zad.txt", 'a', encoding='utf-8') as f:
    f.write('\n-----------------------------------------------------------------------------')
for i in m:
    with open(r"C:\Users\vngorlachev\Downloads\zad.txt", 'a', encoding='utf-8') as f:
        f.write('\n' + i)
print('Преобразованный текст добавлен в файл zad.txt')