from fnmatch import fnmatch

for i in range(0, 10 ** 10, 3013):
    if fnmatch(str(i), '1?6961*5'):
        print(i)