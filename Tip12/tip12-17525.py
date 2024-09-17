s = '9' * 100
while s.count('33333') > 0 or s.count('999') > 0:
    if s.count('33333') > 0:
        s = s.replace('33333', '99', 1)
        #print(len(s))
    else:
        s = s.replace('999', '3', 1)
        #print(len(s))

print(s)