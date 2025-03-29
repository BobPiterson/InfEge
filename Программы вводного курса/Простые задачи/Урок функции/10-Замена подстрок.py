# ПРИМЕР № 10. 
# Дан список строк. Выведите текст, в котором каждая из заданных строк разделена запятой, 
# а если в заданном списке отдельно или в составе строки встречается слово "right", замените его на слово "left"

def left_join(phrases: tuple[str]) -> str:
    s = ''
    for i in phrases:
        s = s + ',' + i.replace('right', 'left')
     
    return s[1:]


print("Пример:")
print(left_join(("left", "right", "left", "stop")))

# These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("Поздравляем, задание выполнено правильно!")
