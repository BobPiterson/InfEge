# Функции с логическими операторами 
# 
def F_and(x, y):
    return x and y

def F_or(x, y):
    return x or y

# Эквивалентность
def Equivalence(x, y):
    return int(x == y)

# Исключающее или
def F_xor(x, y):
    return int(not(x == y))

# Импликация
def Implication(x, y):
    return int(x <= y)

# Обратная Импликация
def ReversImp(x, y):
    return int(x >= y)

for x in range(0,2):
    for y in range(0,2):
        print ('Исходное', x, y, ' AND', F_and(x,y), '  OR', F_or(x,y), '  Эквивалент', Equivalence(x,y), '  XOR', F_xor(x,y), '  Импликация', Implication(x,y), '  ОбратнаяИмпликация', ReversImp(x,y))

# Результат работы:

# Исходное 0 0  AND 0   OR 0   Эквивалент 1   XOR 0   Импликация 1   ОбратнаяИмпликация 1
# Исходное 0 1  AND 0   OR 1   Эквивалент 0   XOR 1   Импликация 1   ОбратнаяИмпликация 0
# Исходное 1 0  AND 0   OR 1   Эквивалент 0   XOR 1   Импликация 0   ОбратнаяИмпликация 1
# Исходное 1 1  AND 1   OR 1   Эквивалент 1   XOR 0   Импликация 1   ОбратнаяИмпликация 1