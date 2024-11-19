for num in range(5):
   print(num)
else:
   print("Числа закончились")
   
for num in range(5):
   print(num)
   if num == 3:
      break # Прервем цикл, если num = 3
else:
   print("Числа закончились")

for num in range(5):
   if num == 3:
      continue # Прервем одну итерацию цикла
   print(num)
else:
   print("Числа закончились")