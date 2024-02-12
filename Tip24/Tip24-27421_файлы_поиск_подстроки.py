# Текстовый файл состоит не более чем из 106 символов X, Y и Z. 
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
count = 0
maxcount = 0
s = open('C:/Users/vngorlachev/Documents/VisualStudioCode/Projects/Новый план/24_demo.txt').read()
for i in range(0, len(s)-1):
    if s[i] != s[i+1]:
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0

print(maxcount + 1)

