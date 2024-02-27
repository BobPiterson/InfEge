# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y) = 0

bi = [0,1]
for x in bi:
    for y in bi:
        for z in bi:
            for w in bi:
                # Внимание! приоритет оператора "<=" выше, чем оператора 'not'. Не забыть 'not w' взять в скобки!
                f = ((x and y) <= (not z or w)) and (((not w) <= x) or not y)
                if f == 0:
                    print('xyzw=',x,y,z,w)
