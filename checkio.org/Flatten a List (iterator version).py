# Taken from mission Flatten a List

from collections.abc import Iterable
def flat_list(array: list[int]) -> Iterable[int]:
    for a in array:
        if isinstance(a, Iterable):
            for b in flat_list(a):
                yield b
        else:
            yield a


if __name__ == "__main__":
    res = flat_list([1, 2, 3])
    assert hasattr(res, "__iter__"), "your function should return the iterator object"
    assert hasattr(res, "__next__"), "your function should return the iterator object"

    assert list(flat_list(iter([1, 2, 3]))) == [1, 2, 3], "First"
    assert list(flat_list(iter([1, iter([2, 2, 2]), 4]))) == [1, 2, 2, 2, 4], "Second"
    assert list(
        flat_list(iter([iter([2]), iter([4, iter([5, 6, iter([6]), 6, 6, 6]), 7])]))
    ) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert list(flat_list(iter([-1, iter([1, iter([-2]), 1]), -1]))) == [
        -1,
        1,
        -2,
        1,
        -1,
    ], "Four"
    print("Done! Check it")