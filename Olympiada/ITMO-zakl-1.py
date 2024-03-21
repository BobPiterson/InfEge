R = (136+136+10**10*(10**10+27))*(10**10+1)//2
print(R)
ans = 0
while R>0:
 ans += R % 10
 R //= 10
print(ans)
