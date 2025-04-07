# Taken from mission Flatten a List

from collections.abc import Iterable
def flat_list(array: list[int]) -> Iterable[int]:
    for a in array:
        if isinstance(a, list):
            for b in flat_list(a):
                yield b
        else:
            yield a


print("Example:")
print(list(flat_list([1, [1]])))

# These "asserts" are used for self-checking
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
