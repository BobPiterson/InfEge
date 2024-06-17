from fnmatch import fnmatch

for i in range(0, 10 ** 8, 273):
    if fnmatch(str(i), '12??36*1'):
        print(i, i // 273)