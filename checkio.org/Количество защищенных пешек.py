def safe_pawns(pawns: set) -> int:
    # Если в наборе всего одна пешка, возвращаем 0
    if len(pawns) == 1:
        return 0
    permittedSymbol = 'abcdefgh'
    # 1) Преобразуем символьную составляющую в соответствующую цифровую и сложим все в список кортежей
    pawns_list = []
    for i in pawns:
        pawns_list.append((permittedSymbol.index(i[0]) + 1, int(i[1])))
    #print(pawns_list)

    # 2) Проверка всех пар пешек и подсчет защищающих друг друга. Складываем все найденные пешки в набор
    # чтобы одна и та же пешка не попала дважды
    steps = set()
    for i in pawns_list:
        for j in pawns_list:
            # параметр [0] означает номер клетки по горизонтали, параметр [1] - по вертикали
            # сравниваются все существующие пары пешек на выполнение условия:
            # если номер клетки 2-й пешки по гориз-ли равен номеру клетки 1-й пешки по горизонтали минус 1 и при этом
            # номер клетки 2-й пешки по вертикали равен номеру клетки 1-й пешки по горизонтали плюс 1,
            # 2-я пешка защищена 1-й пешкой в диагонали вперед и влево
            # аналогично вторым условием проверяем что 2-я пешка защищена 1-й пешкой в диагонали вперед и вправо
            if (j[0] == i[0] - 1 or j[0] == i[0] + 1) and j[1] == i[1] + 1: # слева или справа, но обязательно выше!
                steps.add(j)
                # print('-------------------------------', len(steps), i, j)


    print(len(steps))
    return len(steps)


#print("Example:")
#print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}) == 6
assert safe_pawns({"f4", "e5", "g4", "e4", "b4", "d4", "c4"}) == 1
assert safe_pawns({'h8', 'e5', 'f6', 'a1', 'g7', 'c3', 'b2', 'd4'}) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
