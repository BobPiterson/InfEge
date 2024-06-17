map1 = lambda *args: list(map(*args))
with open('inputs/09.txt', 'r') as file:
    arr = map1(lambda x1: map1(int, x1.split()), file.readlines())

cnt = 0
for line in arr:
    if len(set(line)) == 5:
        even_cnt = 0
        even_sum = 0
        for a in line:
            if a % 2 == 0:
                even_cnt += 1
                even_sum += a

        if (5 - even_cnt) > 2 and (sum(line) - even_sum < even_sum):
            cnt += 1

print(cnt)
