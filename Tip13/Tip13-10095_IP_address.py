# https://kompege.ru/variant
# поразрядная конъюнкция
# на вход подается IP адрес в формате строки, например "192.168.1.1" и маска в формате строки, например "255.255.255.252"
def ip2_to_ip10(s_2):
    tmp = ''
    s_10 = ''
    for i in s_2:
        if i == '.':
            s_10 = s_10 + str(int(tmp,2)) + '.'
            tmp = ''
        else:
            tmp += i
    return s_10[:-1]

def dopoln0(s, length):
    while len(s) < length:
        s = '0' + s
    return s

def conjunction(ip, mask):
    ip += '.'
    mask += '.'
    ip_oct = []
    tmp = ''
    for j in range(len(ip)):
        if ip[j] == '.':
            ip_oct.append(dopoln0(bin(int(tmp))[2:],8))
            tmp = ''
        else:
            tmp += ip[j]

    mask_oct = []
    tmp = ''
    for j in range(len(mask)):
        if mask[j] == '.':
            mask_oct.append(dopoln0(bin(int(tmp))[2:],8))
            tmp = ''
        else:
            tmp += mask[j]

    print('IP address host:', ip_oct)
    print('Mask:           ', mask_oct)

    res_2 = ''
    for i in range(4):
        for j in range(8):
            # Побитовое умножение адреса и маски
            res_2 = res_2 + str(int(ip_oct[i][j]) * int(mask_oct[i][j]))
        res_2 = res_2 + '.'
    return res_2


s_2 = conjunction('192.168.10.18', '255.255.255.240')
print('IP address network:', s_2[:-1], ' = ', ip2_to_ip10(s_2))


