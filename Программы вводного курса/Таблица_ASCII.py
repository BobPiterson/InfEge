# Программа выводит соответствие всех печатаемых символов и их ASCII кодов
# Примечание: с 0 по 31 и 127 коды содержат непечатаемые символы
# from string import digits, ascii_letters
# alp = digits + ascii_letters
print('Символ', ' ', 'Код')
print('-------------')
print('Пробел  ', 32)
for i in range(33, 127):
    print(chr(i), '      ', i)
# for c in alp:
#     print(c, '      ', ord(c))