for i in range(70, 100):
    s = i * 3 - 1

    flag = True
    j = 2
    while j * j <= s:
        if s % j == 0:
            flag = False
            break
        j += 1

    if flag:
        print(i)
        break
