with open('inputs/9.txt', 'r') as f:
    cnt = 0

    for line in f:
        vals = list(map(int, line.split()))
        s = [vals.count(x) for x in vals]
        if s.count(2) == 4 and s.count(1) == 3:
            sm1 = sum(x for x in vals if vals.count(x) == 2) / 4
            sm2 = sum(vals) / 7
            if sm1 < sm2:
                cnt += 1

    print(cnt)
