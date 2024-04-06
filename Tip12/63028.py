'''
1 -> 22
2 -> 12212
3 -> 12
'''

mx = -1
for i in range(50):
    for j in range(50):
        for k in range(50):
            s = '0' + '1' * i + '2' * j + '3' * k + '0'
            while not ('00' in s):
                s=s.replace('01', '220', 1)
                s=s.replace('02', '1013', 1)
                s=s.replace('03', '120', 1)

            if s.count('1') == 13 and s.count('2') == 18 and s.count('3') == 0:
                mx = max(mx, i + j + k + 2)

print(mx)
