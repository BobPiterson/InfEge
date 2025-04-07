# Когда генератор вызывается с помощью функции next, он возвращает следующее значение и "замораживает" своё состояние до следующего вызова.

def prime_numbers(limit):
    num = 2
    while num < limit:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1


for prime in prime_numbers(100):
    print(prime)

