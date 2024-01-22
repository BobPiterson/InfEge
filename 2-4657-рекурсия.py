# Рекурсия
#
#
def f(n : int):
    if n == 1:
        return 1
    else:
        return 2 * g(n - 1) + 5 * n
    
def g(n : int):
    if n == 1:
        return 1
    else:
        return f(n - 1) + 2 * n
    
print(f(4) + g(4))
