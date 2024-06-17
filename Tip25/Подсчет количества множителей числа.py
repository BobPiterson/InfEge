# быстрый алгоритм нахождения множителей числа
import time

def Count_divisor(n: int):
    global start_time, end_time
    # начальное время
    start_time = time.time()

    i = 1
    t = 0
    while i * i <= n:
        if n % i == 0 and i * i != n: 
            t += 2
        elif n % i == 0 and i * i == n: 
            t += 1
        i += 1
    # конечное время
    end_time = time.time()

    return t

print (Count_divisor(97772875200), ',    time = ', end_time - start_time)

