def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Деление на ноль невозможно")
    return x / y

def exponentiation(x, y):
    return x ** y

def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выход")

        choice = input("Введите номер операции (1/2/3/4/5/6): ")

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 6.")
            continue

        if choice == '6':
            print("Выход из программы.")
            break

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Некорректный ввод числа.")
            continue

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Некорректный тип данных. Пожалуйста, введите числа.")

        if choice == '1':
            print("Результат:", addition(num1, num2))
        elif choice == '2':
            print("Результат:", subtraction(num1, num2))
        elif choice == '3':
            print("Результат:", multiplication(num1, num2))
        elif choice == '4':
            try:
                print("Результат:", division(num1, num2))
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == '5':
            print("Результат:", exponentiation(num1, num2))

calculator()
