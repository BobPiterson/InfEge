# https://inf-ege.sdamgia.ru/problem?id=60250
h = [0,2,3,4,5,6,7]
s = set()
count = 0
for a1 in h:
    for a2 in h:
        for a3 in h:
            for a4 in h:
                for a5 in h:
                    s.add(a1)
                    s.add(a2)
                    s.add(a3)
                    s.add(a4)
                    s.add(a5)
                    if len(s) == 5:
                        if not(a1 % 2 == 0 and a2 % 2 == 0 or \
                        a2 % 2 == 0 and a3 % 2 == 0 or \
                        a3 % 2 == 0 and a4 % 2 == 0 or \
                        a4 % 2 == 0 and a5 % 2 == 0 or \
                        a1 % 2 != 0 and a2 % 2 != 0 or \
                        a2 % 2 != 0 and a3 % 2 != 0 or \
                        a3 % 2 != 0 and a4 % 2 != 0 or \
                        a4 % 2 != 0 and a5 % 2 != 0):
                            if a1 != 0:
                                print(a1,a2,a3,a4,a5)
                                count += 1
                    s = set()

print('Ответ =', count)