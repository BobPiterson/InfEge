# ПРИМЕР № 9. Написать тело функции.
# Дан список из любых целых случайных чисел. Выведите список, в котором отсутствуют все уникальные элементы из заданного списка, 
# или выведите пустой список, если в заданном списке все элементы уникальны, 
# например:
# 1) [ 1,2,3,1,3 ] == [ 1,3,1,3 ] («2» - уникальн.)
# 2) [ 1,2,3,4,5 ] == [ ]
# 3) [ 5 , 5 , 5 , 5 , 5 ] == [ 5 , 5 , 5 , 5 , 5 ]
# 4) [10 , 9 , 10 , 10 , 9 , 8] == [10 , 9 , 10 , 10 , 9]

def checkio(data: list[int]) -> tuple:
    out = []
    for i in data:
        if data.count(i) > 1:
            out.append(i)
    return out

print("Пример:")
print(list(checkio([1, 2, 3, 1, 3])))

# These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("Поздравляем, задание выполнено правильно!")