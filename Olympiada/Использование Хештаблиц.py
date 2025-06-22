import hashlib, random, string

def generate_randomstring(length):
    all_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result

# создание хеша
#md5_hash = hashlib.new('md5')

# Получение хеша
#md5_hex = md5_hash.hexdigest()

# Ассоциативный массив
len_array = 100
internal = [None] * len_array

keys = []
print('------------------------------------------------------------------------------------------------------------------------------------------')
# Генерируем ключи словаря
for i in range(10):
    key = 'key'+ str(random.randint(0, 1000)) # генерируем разные ключи словаря
    keys.append(key)
print('Сгенерированные рандомно ключи словаря: ',  keys)


# Хеширование ключа словаря
sha256_hash = hashlib.new('sha256')
print('Полученные хеши от сгенерированных ключей: ', end='')
for i in keys:
    #md5_hash.update(data.encode())
    sha256_hash.update(i.encode())
    index = int(sha256_hash.hexdigest(), 16) % len_array
    print(index, end=',       ')
    
    # Вставка данных
    internal[index] = [i, generate_randomstring(3)]

# вывод полученного массива 
print()
print('Ассоциативный массив:')
print(internal)

# Чтение данных
sha256_hash = hashlib.new('sha256')
print('Повторно полученные хеши ключей: ')
for i in keys:
    sha256_hash.update(i.encode())
    index = int(sha256_hash.hexdigest(), 16) % len_array
    print(index, end=', ')
    print(internal[index])

#print(internal[index])
