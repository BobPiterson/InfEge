def easy_unpack(elements: tuple) -> tuple:
    a = []
    a.append(elements[0])
    a.append(elements[2])
    tmp = list(elements[::-1])
    a.append(tmp[1])
    return tuple(a)


#print("Example:")
#print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")
