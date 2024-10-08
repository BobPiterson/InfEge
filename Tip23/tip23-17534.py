# исполнитель преобразует число X (пусть Х будет числом на экране), у него есть две команды:
# Х - 1,
# Х // 2
# сколько существует таких программ, которые преобразуют исходное число 30
# в число 1, при этом траектория вычислений содержит число 8

# на вход функции подаем исходное число Х и конечное число Y
def f(x, y):
    # если число Х в траектории превысило максимум 9, выходим с результатом 0 (траектория не найдена)
    if x < 1:
        return 0
    # если число Х в траектории стало равно 9, выходим с результатом 1 (траектория найдена)
    if x == y:
        return 1
    # Во всех остальных случаях рекурсивно вызываем функцию со всеми командами, суммируя траектории
    return f(x - 1, y) + f(x // 2, y)

# так как траектория содержит число 8, отдельно подсчитаем количество траекторий от 30 до 8 и от 8 до 1
# ------------------------------------- первая часть - от 30 до 8 ----------------------------------
a1 = f(30, 8)
# ------------------------------------- вторая часть - от 8 до 1 -----------------------------------
a2 = f(8, 1)
# Итоговым количеством траекторий будет произведение количества траекторий от 30 до 8 и количества траекторий от 8 до 1
print(a1 * a2)