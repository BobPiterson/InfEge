# Программа генерирует пароль с цифрами, буквами и спецзнаками
import random
alphabet = [chr(i) for i in range(48, 123)]
#print(alphabet)
#print(random.choice(alphabet))
lenPass = 18
stringPass = ''
for i in range(1, lenPass+1):
    stringPass += random.choice(alphabet)
    if i % 3 == 0:
        stringPass += '-'
print(stringPass)