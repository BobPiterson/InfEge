# https://kompege.ru/variant
# поразрядная конъюнкция
# на вход подается IP адрес в формате строки, например "192.168.1.1" и маска в формате строки, например "255.255.255.252"
def conjunction(ip, mask):
    ip += '.'
    mask += '.'
    ip_oct = []
    tmp = ''
    for j in range(len(ip)):
        if ip[j] == '.':
            if len(tmp) == 1: tmp = '00' + tmp
            if len(tmp) == 2: tmp = '0' + tmp
            ip_oct.append(bin(tmp))
            tmp = ''
        else:
            tmp += ip[j]

    mask_oct = []
    tmp = ''
    for j in range(len(mask)):
        if mask[j] == '.':
            if len(tmp) == 1: tmp = '00' + tmp
            if len(tmp) == 2: tmp = '0' + tmp
            mask_oct.append(bin(tmp))
            tmp = ''
        else:
            tmp += mask[j]

    print(ip_oct, mask_oct)

    res_oct = []
    for i in range(4):
        for j in range(2, 10):
            res_oct.append(str(int(ip_oct[i][j]) * int(mask_oct[i][j])))
    return res_oct

print(conjunction('192.168.10.18', '255.255.255.240'))
