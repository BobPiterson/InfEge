# Пример использования break
# Выйти из цикла после 10 итерации
counter = 0
while True:
    print(counter, "Это бесконечный цикл!")
    counter += 1
    if counter == 10:
        break
