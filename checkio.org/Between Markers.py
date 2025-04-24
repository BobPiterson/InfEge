def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    if text.find(begin) != '' and text.find(end) != '':
        print('---Ok---')
        print(text.find(begin), text.find(end))
        if text.find(begin) >= 0 and text.find(end) >= 0:
            if text.find(begin) > text.find(end):
                return ''
            print(text[text.find(begin)+len(begin):text.find(end)])
            return text[text.find(begin)+len(begin):text.find(end)]

        elif text.find(begin) <= 0 and text.find(end) >= 0:
            print('text.find(begin) ', text.find(begin))
            print(text[0:text.find(end)])
            return text[0:text.find(end)]
        elif text.find(end) <= 0 and text.find(begin) >= 0:
            print('text.find(end) ', text.find(end))
            print(text[text.find(begin)+len(begin):len(text)])
            return text[text.find(begin)+len(begin):len(text)]
        else:
            print('Если нет ни начального маркера, ни конечного:', text)
            return text
             
    return text


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""
assert between_markers("Never send a human to do a machine's job.", 'Never', 'do') == ' send a human to '

print("The mission is done! Click 'Check Solution' to earn rewards!")
