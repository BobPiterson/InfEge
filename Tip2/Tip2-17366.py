# ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x))

table = ['1011', '1010', '1000']
print ('Заданная таблица', table)
s = []
i = 0
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                result = int(((x and w) or (w and z)) == (int(z <= y) and (int(y <= x))))
                if result == 1:
                    s.insert(i, str(x) + str(y) + str(z) + str(w))
                    i += 1
print ('Наборы x,y,z,w:', s)
             