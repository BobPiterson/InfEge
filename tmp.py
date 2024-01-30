
def summa(number):
    sum_tmp = 0
    for i in str(number):
        sum_tmp = sum_tmp + int(i)
    return sum_tmp

n10 = 2123456783 // 8

n2 = bin(n10)[2:]
for i in [1,2,3]:
    if summa(int(n2, 2)) % 2 != 0:
        n2 = n2 + '1'
    else:
        n2 = n2 + '0'
if int(n2,2) > 987654321 and int(n2,2) < 2123456789:
    print(n10, int(n2,2))
