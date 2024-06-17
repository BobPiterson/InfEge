for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            s = '0' + '1' * i + '2' * j + '3' * k
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)

            if s.count('1') == 50 and s.count('2') == 12 and s.count('3') == 7:
                print(i)
