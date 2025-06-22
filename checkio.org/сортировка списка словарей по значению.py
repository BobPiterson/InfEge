def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    # Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
    # Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано в первом
    # аргументе, а сами данные по товарам будут переданы вторым аргументом.
    # Вх. данные: Число и список словарей (int and list of dicts). Каждый словарь имеет 2 ключа "name" и "price".
    # Вых. данные: Такой же как и второй аргумент.


    # отдельная функция, которая возвращает ключи словаря для функции сортировки:
    def get_name(dictionary):
        return dictionary['price']

    # функция get_name многокрано вызывается функцией сортировки
    data.sort(key=get_name, reverse=True)

    # Из сортированного списка забираем первые "limit" значений
    out = []
    for i in range(limit):
        out.append(data[i])

    #print(out)
    return out



assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
