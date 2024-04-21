from fnmatch import *

for i in range(0, 10 ** 10 + 1, 3023):
    if fnmatch(str(i), '1?954*21'):
        print(i)
