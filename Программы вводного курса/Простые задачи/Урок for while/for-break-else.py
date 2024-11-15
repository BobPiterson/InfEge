# Блок else в цикле for выполняется только если цикл не был прерван через break
for x in range(6):
  if x == 5: break
  print(x)
else:
  print("№ 1. Эта строка выполняется, если цикл закончился без Break !")

# Вариант предыдущего кода:
execute_break = False
for x in range(6):
  if x == 5:
    execute_break = True
    break
  print(x)
if not execute_break:
  print("№ 2. Эта строка выполняется, если цикл закончился без Break !")

# ------------------------------------------------------------------------------------------
# Сравните код со следующим циклом, в котором break не срабатывает
print('вариант 2')
for x in range(6):
  if x == 7: break
  print(x)
else:
  print("№ 3. Эта строка выполняется, если весь цикл отработал без Break !")

# Вариант:
execute_break = False
for x in range(6):
  if x == 7:
    execute_break = True
    break
  print(x)
if not execute_break:
  print("№ 4. Эта строка выполняется, если весь цикл отработал без Break !")
