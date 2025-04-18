def adjacent_letters(line: str) -> str:
    #print('----------------------------------')
    #print(line)
    if len(line) < 2:
        return line

    line = line + '.'
    out_string = ''
    # перебор начальной строки
    x = 1
    previous = line[0]
    overlap = False
    while x < len(line):
        #print('до проверки, X =', x, 'previous: ', previous, ' line[x]: ', line[x])
        if previous == line[x]:
            x += 1
            #print('Совпали буквы с индексами ------------> X =', x - 2, ',', x -1)
            overlap = True
        else:
            out_string = out_string + previous
        previous = line[x]
        x += 1
        #print('out_string: ', out_string, ' X =', x, 'previous: ', previous)
    out_string = out_string + previous
    #print(out_string[:-1])
    out = out_string[:-1]
    if overlap:
        return adjacent_letters(out)
    else:
        return out


# print("Example:")
# print(adjacent_letters("abbacee"))
print(adjacent_letters("abbaca"))

assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""
print("The mission is done! Click 'Check Solution' to earn rewards!")