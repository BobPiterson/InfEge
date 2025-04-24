def cut_sentence(line: str, length: int) -> str:
    if len(line) <= length: return line
    s_list = line.split(' ')
    #print(s_list)
    s = ''
    for i in s_list:
        #print(len(s), length - len(i))
        if len(s) - 1 < length - len(i):
            s = s + i + ' '
        else:
            break
    #print(s[:-1] + '...')
    return s[:-1] + '...'


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
assert cut_sentence('Hi my name is Alex', 9) == 'Hi my...'
assert cut_sentence('Hi my name is Alex', 10) == 'Hi my name...'

print("The mission is done! Click 'Check Solution' to earn rewards!")