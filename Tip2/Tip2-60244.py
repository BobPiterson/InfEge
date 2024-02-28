# https://inf-ege.sdamgia.ru/problem?id=60244
# w, x, y, z
# (x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w = 0
bi = [0,1]
for w in bi:
    for x in bi:
        for y in bi:
            for z in bi:
                f = (x and (not y)) or (y == z) or (not w)
                if f == 0:
                    print(w, x, y, z)