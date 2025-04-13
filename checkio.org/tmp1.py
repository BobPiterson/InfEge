def letter_queue(commands: list[str]) -> str:
    print('-------------------------------------')
    print(commands)
    out = []
    for i in commands:
        if 'PUSH' in  i:
            out.append(i[5:])
        elif 'POP' in i and len(out) != 0:
            out.pop(0)
        else:
            print('Список пуст!')
        print(out)

    return ''.join(out)


print("Example:")
print(
    letter_queue(
        ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
    )
)

# These "asserts" are used for self-checking
assert (
    letter_queue(
        ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
    )
    == "DOT"
)
assert letter_queue(["POP", "POP"]) == ""
assert letter_queue(["PUSH H", "PUSH I"]) == "HI"
assert letter_queue([]) == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
