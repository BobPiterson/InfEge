def missing_number(items: list[int]) -> int:
    s_list = sorted(items)
    step = (s_list[-1] - s_list[0]) // len(s_list)
    #print(s_list, step)
    for i in range(1, len(s_list)):
        if s_list[i] - s_list[i - 1] != step:
            missing = s_list[i - 1] + step
            #print(missing)
            break
    return missing


#print("Example:")
#print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
