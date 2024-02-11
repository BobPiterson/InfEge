import time
ddos = []
serv = []
zapr = [1,1,2, 1,1,2, 1,1,2]
count0 = 0
count1 = 0
count2 = 0

for i in range(0, 200):
    #time.sleep(0.1)
    # Обработка очереди DDoS
    if i % 15 == 0:
        # Каждые 15 мс ставим в очередь запрос от пользователя
        if len(zapr) > 0:
            ddos.append(zapr.pop(0))
            print('Время = ', i, 'Поступил запрос от пользователя в DDoS', ' ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)

    if i < 30:
        #print(ddos)
        # каждую 1 мс ставим в очередь запрос от злоумышленника
        ddos.append(0)
        #print('Время = ', i, 'Поступил запрос от -----злоумышленника----- в DDoS', ddos, 'serv = ', serv, 'zapr = ', zapr)
        if i % 2 == 0 and i != 0:
            # в первые 30 секунд каждые 2 мс обрабатываем очередь ddos
            if len(ddos) > 0:
                serv.append(ddos[0])
                ddos.remove(ddos[0])
            print('Время = ', i, 'Запрос из DDoS типа ', serv[len(serv)-1],' отправлен Серверу, ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)
    else:
        ddos.append(0)
        #print('Время = ', i, ' - Поступил запрос от -----злоумышленника----- в DDoS', ' ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)
        if (i + 20) % 50 == 0 and ddos[0] == 0:
            serv.append(ddos[0])
            ddos.remove(ddos[0])
            print('Время = ', i, 'Запрос злоумышленника из DDoS отправлен Серверу, ----------------------------------------- ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)
        elif ddos[0] == 0:
            ddos.remove(ddos[0])
            #print('Время = ', i, 'Запрос злоумышленника в DDoS Заблокирован, ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)

        elif ddos[0] == 1 or ddos[0] == 2:
            serv.append(ddos[0])
            ddos.remove(ddos[0])
            print('Время = ', i, 'Запрос Юзера ', serv[len(serv)-1],' из DDoS отправлен Серверу, ddos = ', ddos, 'serv = ', serv, 'zapr = ', zapr)

    # Обработка очереди сервера
    if count2 == 0 and count1 == 0 and count0 == 0:
        if len(serv) > 0 and serv[0] == 2:
            serv.remove(serv[0])
            print('Время = ', i, 'serv = ', serv, 'Сервер начал определение типа (3 мс) и обработку запроса типа 2 (12 мс)')
            count2 = 12 + 2
            
        elif len(serv) > 0 and serv[0] == 1:
            serv.remove(serv[0])
            print('Время = ', i, 'serv = ', serv, 'Сервер начал определение типа (3 мс) и обработку запроса типа 1 (6 мс)')
            count1 = 6 + 2
            
        elif len(serv) > 0 and serv[0] == 0:
            serv.remove(serv[0])
            print('Время = ', i, 'serv = ', serv, 'Сервер начал определение типа (3 мс) запроса от злоумышленника')
            count0 = 2
    else:
        if count0 != 0:
            count0 -= 1
            if count0 == 0:
                print('Время = ', i, 'Сервер определил тип запроса: 0 и отклонил обработку запроса от злоумышленника')
        elif count1 != 0:
            count1 -= 1
            if count1 == 0:
                print('Время = ', i, 'Сервер определил тип запроса: 1 и закончил обработку запроса от Юзера тип 1 (3 + 6 мс)')
        elif count2 != 0:
            count2 -= 1
            if count2 == 0:
                print('Время = ', i, 'Сервер определил тип запроса: 2 и закончил обработку запроса от Юзера тип 2 (3 + 12 мс)')
                if len(zapr) == 0:
                    print('Очередь запросов пользователя закончилась за ', i+1, ' mc')
                    break









