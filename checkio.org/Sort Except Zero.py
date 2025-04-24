from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    print('------------------------------------------')
    print(items)
    without_zeros = []
    places_zeros = []
    for i in range(len(items)):
        if items[i] != 0:
            without_zeros.append(items[i])
        else:
            places_zeros.append(i)
    sorted_wz = sorted(without_zeros)
    print(sorted_wz)
    out = []
    for i in range(len(items)):
        if not i in places_zeros:
            out.append(sorted_wz.pop(0))
        else:
            out.append(0)
    print(out)     
    return out


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")