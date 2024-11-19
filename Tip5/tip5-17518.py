for n in range (100):
    b = bin(n)[2::]
    
    if b.count('1') % 2 == 0:
        s = b + '0'
        s = '10' + s[2::]
    else:
        s = b + '1'
        s = '11' + s[2::]
    print(n, b, s, int(s, 2))

