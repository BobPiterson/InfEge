def between_markers(text: str, start: str, end: str) -> str:
    a = []
    inside_text = False
    for c in text:
        if c == start:
            inside_text = True
            continue
        elif c == end:
            inside_text = False
        if inside_text:
            a.append(c)

    return ''.join(a)


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
