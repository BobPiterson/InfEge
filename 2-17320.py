# ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z)) 
table = ['0111', '0101', '0100']
res = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x and y) or (y and z)) == ((x <= w) and (w <= z))) == 1:
                    res.append(str(x)+str(y)+str(z)+str(w))
print(res)
print(' ')

vars = ['x', 'y', 'z', 'w']
index = [0,1,2,3]
set1 = set()
i = 0
for a1 in index:
    for a2 in index:
        for a3  in index:
            for a4 in index:
                set1.add(a1)
                set1.add(a2)
                set1.add(a3)
                set1.add(a4)
                if len(set1) == 4:
                    for k in res:
                        #print(k[a1]+k[a2]+k[a3]+k[a4])
                        if table[0] == k[a1]+k[a2]+k[a3]+k[a4] and table[1] == k[a1]+k[a2]+k[a3]+k[a4] and table[2] == k[a1]+k[a2]+k[a3]+k[a4]:
                            #print('Решение найдено!') 
                            print(k[a1]+k[a2]+k[a3]+k[a4])
                            
                    i += 1
                set1 = set()
#print(i)