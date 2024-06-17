def divisors(x):
    divs = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)

    return sorted(divs)


ans = 0
mx = 0
for i in range(120115, 120201):
   l = len(divisors(i))
   if l > mx:
       mx = l
       ans = i

print(len(divisors(ans)), ans)