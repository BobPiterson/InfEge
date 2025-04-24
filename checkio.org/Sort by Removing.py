def sort_by_removing(values: list) -> list:
    if len(values) == 0:
        return values
    if len(values) == 1:
        return values
    maximum = values[0]
    out = [values[0]]
    print(out, maximum)
    for i in range(1, len(values)):
        if values[i] >= values[i - 1] and values[i] >= maximum:
            out.append(values[i])
            maximum = values[i]
    print('-------------------> ', out, maximum)
    return out


if __name__ == "__main__":
    #print("Example:")
    #print(sort_by_removing([3, 5, 2, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_removing([3, 5, 2, 6]) == [3, 5, 6]
    assert sort_by_removing([7, 6, 5, 4, 3, 2, 1]) == [7]
    assert sort_by_removing([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert sort_by_removing([5, 6, 7, 0, 7, 0, 10]) == [5, 6, 7, 7, 10]
    assert sort_by_removing([1, 5, 2, 3, 4, 7, 8]) == [1, 5, 7, 8]
    assert sort_by_removing([1, 7, 2, 3, 4, 5]) == [1, 7]
    assert sort_by_removing([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
