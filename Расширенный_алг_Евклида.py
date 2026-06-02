def extended_gcd(a, b):
    """
    Возвращает (gcd, x, y) такие что a*x + b*y = gcd
    Использует итеративный расширенный алгоритм Евклида.
    """

    x2 = 1   # коэффициенты при a
    x1 = 0       # коэффициенты при a
    y2 = 0   # коэффициенты при b
    y1 = 1       # коэффициенты при b

    print('old_r,r,old_x,x,old_y,y = ', a,b,x2,x1,y2,y1)
    while b != 0:
        print('-----------------------------')
        q = a // b
        print(q)
        tmp = a
        a = b
        b = tmp % b
        print(b, a)
        tmp = x2
        x2 = x1
        x1 = tmp -  q * x1
        print(x1, x2)
        tmp = y2
        y2 = y1
        y1 = tmp -  q * y1
        print(y1, y2)
        print('-----------------------------')
    print(a, x2, y2)
    return a, x2, y2

def find_rsa_d(e, phi):
    # Для устойчивости сразу берём e по модулю phi
    e_mod = e % phi
    gcd, x, y = extended_gcd(e_mod, phi)

    if gcd != 1:
        raise ValueError("e и φ(n) не взаимно просты. Обратный элемент не существует.")

    # x может быть отрицательным, приводим к положительному остатку
    d = x % phi
    return d

# Исходные данные
e = 17
phi = 360

d = find_rsa_d(e, phi)
print(f"Экспонента расшифрования d = {d}")
# Проверка
assert (e * d) % phi == 1, "Ошибка проверки!"
print(f"Проверка: (e * d) mod φ(n) = {(e * d) % phi} ✅")