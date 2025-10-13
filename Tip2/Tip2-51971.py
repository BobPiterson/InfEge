# (x ≡ ¬y) → ((z → ¬w) ∧ (w → y))
#Пер 1  Пер 2   Пер 3   Пер 4   Функция
#???	???	    ???	    ???	    F
#1	    1	    0	    1	    1
#0		        0		        0
#			            0	    0

print("x y z w  =  F")
bi = [0,1]
for x in bi:
    for y in bi:
        for z in bi:
            for w in bi:
                # Внимание! приоритет оператора "<=" выше, чем оператора 'not'. Не забыть 'not y', 'not w' взять в скобки!
                f = (x == (not y)) <= ((z <= (not w)) and (w <= y))
                if f == 0:
                    print(x,y,z,w,' = ',int(f))
                else:
                    print(x,y,z,w,' = ',int(f))
