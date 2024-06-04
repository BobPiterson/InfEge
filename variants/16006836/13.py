for i in range(9):
    ls = i * '1' + (8 - i) * '0'
    ls10 = int(ls, 2)
    print(ls, 139 & ls10, 154 & ls10)