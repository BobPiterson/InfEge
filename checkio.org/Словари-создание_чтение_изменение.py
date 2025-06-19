def popular_words(text: str, words: list) -> dict:
    # Вся символы строки переводятся в нижний регистр,
    # затем убирается мусор в виде перевода строки,  заменяя его на пробел,
    # затем из оставшихся слов, разделенных пробелами, формируется список
    all_words = text.lower().replace('\n', ' ').split(' ')
    print(all_words)
    # создаем словарь из заданных слов в качестве ключей и нулей в качестве значений всех ключей
    dic = {a: 0 for a in words}
    #print(dic)
    for w in all_words:
        if w in words:
            # изменяем словарь, добавляя 1 к значению указанного ключа w
            dic.update({w: dic.get(w) + 1})

    #print(dic)
    return dic


print("Example:")
print(
    popular_words(
        """
When I was One
I had just begun
When I was Two
I was nearly new
""",
        ["i", "was", "three", "near"],
    )
)

assert popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}

print("The mission is done! Click 'Check Solution' to earn rewards!")