# пример не используя elif
score = int(input("Введите количество набранных баллов: "))

if score >= 90:
    print("Отлично! Ваша оценка: 5")
else:
    if score >= 70:
        print("Здорово! Ваша оценка: 4")
    else:
        if score >= 60:
            print("Не так как хотелось бы! Ваша оценка - твердая 3")
        else:
            if score >= 50:
                print("Ваша оценка: 3-. Стоит повторить материал.")
            else:
                print("Вы не сдали экзамен")


# пример c elif
score = int(input("Введите количество набранных баллов: "))

if score >= 90:
    print("Отлично! Ваша оценка: 5")
elif score >= 70:
    print("Здорово! Ваша оценка: 4")
elif score >= 60:
    print("Не так как хотелось бы! Ваша оценка - твердая 3")
elif score >= 50:
    print("Ваша оценка: 3-. Стоит повторить материал.")
else:
    print("Вы не сдали экзамен")