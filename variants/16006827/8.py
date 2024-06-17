from itertools import permutations

cnt = 0
cnt2 = 0
for i in permutations('МАТВЕЙ', r=6):
    x = ''.join(i)
    if 'АЕ' in x:
        cnt2 += 1
    if x[0] != 'Й' and 'АЕ' not in x:
        cnt += 1

print(cnt2)
print(cnt)
