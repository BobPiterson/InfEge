def atbash(plaintext: str) -> str:
    ope = 'abcdefghijklmnopqrstuvwxyz'
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    for i in plaintext:
        if i in ope:
            s = s + chr(122 + 97 - ord(i))
        elif i in upp:
            s = s + chr(90 + 65 - ord(i)) 
        else:
            s = s + i
    #print(s)
    return s


if __name__ == "__main__":
    #print("Example:\nplaintext: testing")
    #print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")
