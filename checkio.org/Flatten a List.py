def goes_after(word: str, first: str, second: str) -> bool:
    print('----', first, second)
    print(word.find(first))
    if word.find(first) >= 0 and len(word) > word.find(first) + 1:
        print(word[word.find(first) + 1])
        if word.find(first) + 1 == word.find(second):
            return True
    
    return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False
assert goes_after('transport', 'r', 't') == False
assert goes_after('almaz', 'm', 'a') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
