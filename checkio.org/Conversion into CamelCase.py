def to_camel_case(name: str) -> str:
    s = name[0].upper()
    for i in range(1, len(name)):
        #print(s, name[i - 1], name[i])
        if name[i - 1] == '_':
            s = s[:-1] + name[i].upper()
        else:
            s = s + name[i]
    #print(s)
    return s


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")