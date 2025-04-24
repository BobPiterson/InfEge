def is_all_upper(text: str) -> bool:
    if text == '': return True
    for i in text:
        if not (i.isupper() or i.isspace() or i.isnumeric()):
            return False
    return True

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
