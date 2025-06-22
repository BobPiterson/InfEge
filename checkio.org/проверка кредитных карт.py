def checker(card: str) -> bool:
    a = []
    for i in card:
        if i != ' ':
            a.append(int(i))
    #print(a)
    b = []
    for i in range(len(a)):
        if i % 2 == 0:
            tmp = a[i] * 2
            if tmp > 9:
                tmp = tmp % 10 + tmp // 10
            b.append(tmp)
        else:
            b.append(a[i])
    #print(b)
    if sum(b) % 10 == 0:
        return True
    return False


#print("Example:")
#print(checker("4137 8947 1175 5904"))

# These "asserts" are used for self-checking
assert checker("4137 8947 1175 5904") == True
assert checker("5468 1234 5678 9123") == False
assert checker("4539 1488 0343 6467") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
