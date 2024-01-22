# ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z))
#
table = ['0111', '0101', '0100']
#print ('Заданная таблица', table)
s = []
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                result = int(((x and y) or (y and z)) == (int(x <= w) and (int(w <= z))))
                if result == 1:
                    s.append(str(x) + str(y) + str(z) + str(w))

#print ('Наборы x,y,z,w:', s)

vars = ['x','y','z','w']
num = [0,1,2,3]
n = set()
i = 0
for a1 in num:
    for a2 in num:
        for a3 in num:
            for a4 in num:
                n.add(a1)
                n.add(a2)
                n.add(a3)
                n.add(a4)
                if len(n) == 4:
                    print(vars[a1], vars[a2], vars[a3], vars[a4], end = " ")
                    for q in s:
                        kom = q[a1]+q[a2]+q[a3]+q[a4]
                        if (kom == table[0]) or (kom == table[1]) or (kom == table[2]):
                            print(kom, end = " ")
                    print('')
                    i += 1
                n = set()
#print(i)

