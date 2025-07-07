def safe_pawns(pawns: set) -> int:
    # Если в наборе всего одна пешка, возвращаем 0
    if len(pawns) == 1:
        return 0
    permittedSymbol = 'abcdefgh'
    # 1) Преобразуем символьную составляющую в соответствующую цифровую и сложим все в список кортежей
    pawns_list = []
    for i in pawns:
        pawns_list.append((permittedSymbol.index(i[0]) + 1, int(i[1])))
    print(pawns_list)

    # 2) Сортируем по второму параметру (по вертикальной координате),
       # сортировка нужна, чтобы координаты пешек всегда были от меньшего к большему, чтобы проверять
       # соседство только прибавляя вертикальную координату, но не вычитая
       # отдельная функция, которая возвращает второй элемент списка для функции сортировки:
    def get_name(list1):
        return list1[1]
    # функция get_name многокрано вызывается функцией сортировки
    pawns_list.sort(key=get_name)
    print(pawns_list)

    # 3) Проверка всех пар пешек и подсчет защищающих друг друга. Складываем все защищенные пешки в набор
    # чтобы одна и та же пешка не попала дважды
    steps = set()
    for i in range(0, len(pawns_list)):
        for j in range(i, len(pawns_list)):
            #print('1:', pawns_list[j][0], '  2:', pawns_list[i][0] - 1, '  3:', pawns_list[j][1], '  4:', pawns_list[i][1] + 1)

            if pawns_list[j][0] == pawns_list[i][0] - 1 and pawns_list[j][1] == pawns_list[i][1] + 1 or \
            pawns_list[j][0] == pawns_list[i][0] + 1 and pawns_list[j][1] == pawns_list[i][1] + 1:
                steps.add(pawns_list[j])
                print('-------------------------------', len(steps), pawns_list[i], pawns_list[j])
                

    print(len(steps))
    return len(steps)


#print("Example:")
#print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}) == 6
assert safe_pawns({"f4", "e5", "g4", "e4", "b4", "d4", "c4"}) == 1
assert safe_pawns({'h8', 'e5', 'f6', 'a1', 'g7', 'c3', 'b2', 'd4'}) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
