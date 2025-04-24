from collections.abc import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    a = dict()
    for i in items:
        a[i] = items.count(i)
    #print('Исходный ', a)
    sorted_a1 = sorted(a.items(), key=lambda item: item[1], reverse=True)
    #print(sorted_a1)
    b = []
    for i in sorted_a1:
        count = i[1]
        while count > 0:
            b.append(i[0])
            count -= 1  

    return b


# print("Example:")
print(list(frequency_sort([6, 2, 2, 6, 4, 4, 4])))

assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")

