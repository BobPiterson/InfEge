def extended_gcd(a, b):
    """
    Возвращает (gcd, x, y) такие что a*x + b*y = gcd
    Использует итеративный расширенный алгоритм Евклида.
    """
    old_r = a
    r = b
    old_x = 1   # коэффициенты при a
    x = 0       # коэффициенты при a
    old_y = 0   # коэффициенты при b
    y = 1       # коэффициенты при b

    print('old_r,r,old_x,x,old_y,y = ', old_r,r,old_x,x,old_y,y)
    while r != 0:
        print('-----------------------------')
        quotient = old_r // r
        print(quotient)
        tmp = old_r
        old_r = r
        r = tmp % r
        # old_r, r = r, old_r - quotient * r
        print(old_r, r)
        tmp = old_x
        old_x = x
        x = tmp -  quotient * x
        #old_x, x = x, old_x - quotient * x
        print(old_x, x)
        tmp = old_y
        old_y = y
        y = tmp -  quotient * y
        #old_y, y = y, old_y - quotient * y
        print(old_y, y)
        print('-----------------------------')
    return old_r, old_x, old_y

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
e = 65537
phi = 360

d = find_rsa_d(e, phi)
print(f"Экспонента расшифрования d = {d}")
# Проверка
assert (e * d) % phi == 1, "Ошибка проверки!"
print(f"Проверка: (e * d) mod φ(n) = {(e * d) % phi} ✅")