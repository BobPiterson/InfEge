from fnmatch import fnmatch

for i in range(0, 10 ** 10, 2024):
    if fnmatch(str(i), '3?6906*4'):
        print(i)
