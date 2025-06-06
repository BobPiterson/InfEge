def adjacent_letters(line: str) -> str:
    print('-----------------------------------')
    print(line)
    if len(line) < 2:
        return line
    
    tmp = line
    out = ''
    i = 1
    while i < len(line):

        if line[i - 1] == line[i]:
            i = i + 3
            print('------------', line[i - 4], line[i - 3])

        else:
            i = i + 1
        tmp = line[i - 2]

        print('tmp =', tmp)
        
        out = out + tmp
        print('out =', out  + line[-1:])

       
    return ""


#print("Example:")
#print(adjacent_letters("abbaca"))

# These "asserts" are used for self-checking
assert adjacent_letters("letters") == "lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")