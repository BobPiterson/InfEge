ddos = []
serv = []
zapr = [1,1,2, 1,1,2, 1,1,2]
count = 0
tip = -1

for i in range(0, 200):
    # Поступление запросов в DDoS
    # каждую 1 мс ставим в очередь запрос от злоумышленника, независимо от всего остального
    ddos.append(0)
    #print('Время = ', i, 'Поступил запрос от -----злоумышленника----- в DDoS', ddos, 'serv = ', serv, 'zapr = ', zapr)
    # Каждые 15 мс ставим в очередь запрос от пользователя
    if i % 15 == 0:
        if len(zapr) > 0:
            ddos.append(zapr.pop(0))
            print('Время = ', i, 'DDoS:   Поступил запрос от пользователя', f' {ddos=} ', 'serv = ', serv, 'zapr = ', zapr)


    # Обработка очереди DDoS
    if i > 1 and i < 30:
        if i % 2 == 0:
            # Первые 30 запросов каждые 2 мс обрабатываем очередь ddos
            serv.append(ddos[0])
            print('Время = ', i, 'Сервер: Поступил запрос типа ', ddos[0], ', ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)
            ddos.remove(ddos[0])

    if i >= 30:
        if ddos[0] == 1 or ddos[0] == 2:
            serv.append(ddos[0])
            print('Время = ', i, 'Сервер: Поступил запрос типа ', ddos[0], ', ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)
            ddos.remove(ddos[0])

        if ddos[0] == 0:
            if (i + 20) % 50 == 0 and i != 30:
                serv.append(ddos[0])
                print('Время = ', i, 'Сервер: Поступил 50-й запрос типа ', ddos[0], ', ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)
            ddos.remove(ddos[0])
            #print('Время = ', i, 'Запрос злоумышленника в DDoS Заблокирован, ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)

    # Обработка очереди сервера
    # Если сервер ничего не обрабатывает
    if count == 0:
        if len(serv) > 0: 
            tip = serv[0]
            if tip == 2:
                count = 12 + 3
            if tip == 1:
                count = 6 + 3
            if tip == 0:
                count = 3
            # Удалим запрос из очереди сервера
            serv.remove(tip)
            print('Время = ', i, 'Сервер начал обработку запроса типа ', tip, ' и удалил его из очереди, serv = ', serv)

    # Если сервер занят обработкой запроса
    else:
        count = count - 1
        if count == 0:
            print('Время = ', i, 'Сервер завершил обработку запроса типа ', tip)
            if len(zapr) == 0 and len(serv) == 0:
                print('Очередь запросов пользователя закончилась за ', i+1, ' mc')
                break









