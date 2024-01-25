def f_left(x,a):
    return ((x in a) <= (x**2 <= 81))
def f_right(x,a):
    return ((x**2 <= 36) <= (x in a))

a = set()
for i in range(-10, 11):
    #a.add(i)
    print(i, end='\t')
print("")
# Переберем все значения х и проверим результат функции:
for x in range(-10, 11):
     print(f_left(x,a), end='\t')
print("")
for x in range(-10, 11):
     print(f_right(x,a), end='\t')
print("------------------------------------------------------------------------------------------------------------------------------------------")
for x in range(-10, 11):
     print(f_left(x,a) and f_right(x,a), end='\t')
print("")