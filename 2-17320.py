# ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z)) 
table = ['0111', '0101', '0100']
res = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x and y) or (y and z)) == ((x <= w) and (w <= z))) == 1:
                    res.append(str(x)+str(y)+str(z)+str(w))
#print(res)

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
                    s0 = table[0][a1] + table[0][a2] + table[0][a3] + table[0][a4]
                    s1 = table[1][a1] + table[1][a2] + table[1][a3] + table[1][a4]
                    s2 = table[2][a1] + table[2][a2] + table[2][a3] + table[2][a4]  
                    if s0 in res and s1 in res and s2 in res:
                        print(vars[a1] + vars[a2] + vars[a3] + vars[a4])
                set1 = set()
