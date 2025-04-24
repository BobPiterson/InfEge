def translation(text: str) -> str:
    soglas = 'bcdfghjklmnpqrstvwxz'
    glas = 'aeiouy'
    tlist = text.split()
    print(tlist)
    out = []
    for word in tlist:
        count = 0
        if len(word) == 2:
            s = word[0]
            out.append(s)
            continue
        if len(word) == 3:
            s0 = word[0]
            s1 = word[1]
            s2 = word[2]
            if s0 == s1 and s0 == s2:
                s = s0
                out.append(s)
                continue
            else:
                print('Ошибка, Слово: ', word)

        if len(word) > 3:
            s0 = word[0]
            s1 = word[1]
            s2 = word[2]
            if s0 == s1 and s0 == s2:
                s = s0
            elif s0 in soglas and s1 in glas and s2 in soglas:
                s = s0 + s2
            elif s0 in soglas and s1 in glas and s2 in glas:
                s = s0
                count = 2
        
            for i in range(3, len(word)):
                if word[i] in glas and word[i - 1] in glas and count == 2:
                    s = s + word[i]
                    count = 0
                elif word[i] in glas and word[i - 1] in glas and count < 2:
                    count += 1
                    continue
                elif word[i] in glas and word[i - 1] in soglas:
                    continue
                else:
                    s = s + word[i] 
                print(s)
        out.append(s)
    s_out = ''
    for k in out:
        s_out = s_out + k + ' '
    print('-------------------->', s_out[:-1])
    return s_out[:-1]


#print("Example:")
#print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
