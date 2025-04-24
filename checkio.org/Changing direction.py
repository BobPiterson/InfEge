def changing_direction(elements: list[int]) -> int:
    count = 0
    #print('----------------------------------------------------')
    if len(elements) <= 2:
        return 0
    if elements[1] - elements[0] > 0:
         direct = "up"
    elif elements[1] - elements[0] < 0:
        direct = "down"
    else:
        direct = 'flat'
    #print(elements[0], elements[1], direct, count)
    for i in range(2, len(elements)):
        
        if elements[i] - elements[i - 1] > 0 and direct == "down":
            count += 1
            direct = "up"
        elif elements[i] - elements[i - 1] > 0:
            direct = "up"
        elif elements[i] - elements[i - 1] < 0 and direct == "up": 
            count += 1
            direct = "down"
        elif elements[i] - elements[i - 1] < 0:
            direct = "down"
        #print(elements[i - 1], elements[i], direct, count)
    return count

#print("Example:")
#print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")

