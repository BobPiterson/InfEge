# Программа выводит все простые числа в указанном диапазоне и сообщает их количество
start = 2 # Меньше 2 не ставить!
#stop = 1_000_000 # Больше 1_000_000 долго считает!
stop = 1500
prime = []
def isPrime(n) -> bool:
    # передаем в функцию число из указанного диапазона, назовем его n
    # Переберем все числа от 2 до корня от n и проверяем, делится ли n на какое нибудь число без остатка
    # если проверили все числа, и n не поделилось без остатка, функция возвращает True,  значит число n - простое
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(start, stop + 1):
    if isPrime(i):
        prime.append(i)

print(sorted(prime))
print('Найдено простых чисел: ', len(prime))


