# Микрокалькулятор для одного действия. 
# Напишите программу, которая вводит два целых числа и один символ (одну математическую операцию). 
# Если этот символ является обозначением одной из четырёх математических операций (+, -, *, /), 
# то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция». 
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

x = int(input())
y = int(input())
oper = input()

if oper == '+':
    result = x + y
elif oper == '-':
    result = x - y
elif oper == '*':
    result = x * y
elif oper == '/':
    if y != 0:
        result = x / y
    else:
        print('На ноль делить нельзя!')
        exit(0) 
else:
    print('Неверная операция')
    exit(0)

print(result)