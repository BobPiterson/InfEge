from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    print('--------------------------------------')
    out = []
    d = {}
    for i in numbers:
        d[i] = numbers.count(i)
    #print(d)

    sorted_d = dict(sorted(sorted(d.items(), key=lambda x : x[0]), key=lambda x : x[1], reverse=True))
    print(sorted_d)

    for key, val in sorted_d.items():
        out.extend([key for _ in range(val)])
    print(out)
    return out


#print("Example:")
#print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
#assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")