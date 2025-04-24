def how_deep(tup: tuple) -> int:
    if not isinstance(tup, tuple):
        return 0
    if not tup:
        return 1
    max_depth = 0
    for item in tup:
        current_depth = how_deep(item)
        if current_depth > max_depth:
            max_depth = current_depth
    return max_depth + 1

#print("Example:")
#print(how_deep((1, 2, 3)))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")