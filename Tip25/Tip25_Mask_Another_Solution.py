x = 0
while x < 1e12:
    s = str(x)
    if len(s) >= 10 and s[0:2] == '12' and s[3] == '3' and s[-1] == '9' and s[-6:-3] == '456':
        print(x, x // 98591)
    x += 98591
