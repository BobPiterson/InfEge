# Для какого наибольшего целого положительного числа А выражение
# (x & a == 0) or not(x & 37 == 0) or not(x & 12 == 0)
# тождественно истинно при любых целых положительных Х?
# где x & a - поразрядная конъюнкция 

def res(a):
    result = True
    for x in range(1, 1000):
        f = (x & a == 0) or not(x & 37 == 0) or not(x & 12 == 0)
        result = result and f
    return result

a_max = 0
for a in range(1, 1000):
    if res(a):
        if a_max < a:
            a_max = a
print(a_max)