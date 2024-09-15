# Программа находит все простые числа в указанном диапазоне
start = 2 # Меньше 2 не ставить!
stop = 1_000_000 # Больше 1_000_000 долго считает!
prime = []
def isPrime(n) -> bool:
    # Переберем все числа от 2 до корня от искомого числа
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(start, stop + 1):
    if isPrime(i):
        prime.append(i)

#print(sorted(prime))
print('Найдено простых чисел: ', len(prime))


