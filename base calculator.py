num1 = float(input("Введите первое число: "))

operation = input("Введите операцию (+, -, *, /): ")

num2 = float(input("Введите второе число: "))

if operation == "+":
    result = num1 + num2
    print("Результат:", result)

elif operation == "-":
    result = num1 - num2
    print("Результат:", result)

elif operation == "*":
    result = num1 * num2
    print("Результат:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Результат:", result)
    else:
        print("Ошибка: на ноль делить нельзя")

else:
    print("Неизвестная операция! Выберите +, -, * или /.")