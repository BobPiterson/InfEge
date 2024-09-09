count = 0
for n in range(4096, 32768):
    s = oct(n)[2::]
    if int(s[0]) % 2 == 0:
        if s[4] != '2' and s[4] != '6':
            if s.count('7') <= 2:
                count += 1
                if n < 15000: print(s)

print(count)
