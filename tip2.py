# ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z)) 
table = ['0111', '0101', '0100']
# ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)) 
# table = ['1011', '1000', '1010']
# print(table)

res = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x and y) or (y and z)) == ((x <= w) and (w <= z))) == 1:
                # if (((x and w) or (w and z)) == ((z <= y) and (y <= x))) == 1:
                    res.append(str(x)+str(y)+str(z)+str(w))
# print(res)

vars = ['x', 'y', 'z', 'w']
index = [0,1,2,3]
set1 = set()
for a1 in index:
    for a2 in index:
        for a3  in index:
            for a4 in index:
                set1.add(a1)
                set1.add(a2)
                set1.add(a3)
                set1.add(a4)
                if len(set1) == 4:
                    m = ''
                    i = 0
                    for k in range(len(res)):
                        m = res[k][a1] + res[k][a2] + res[k][a3] + res[k][a4]
                        if m in table:
                            i += 1
                    if i == len(table): 
                        print(vars[a1] + vars[a2] + vars[a3] + vars[a4])       
                set1 = set()
