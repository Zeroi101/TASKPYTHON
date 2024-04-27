#coding=windows-1251
while True:
    user_input = input("Введите число:")

    if user_input == 'exit':
        print("Программа завершена.")
        break
    
    try:
        number = int(user_input)
        length = len(str(number))
        print("Длина числа:", length)
    except ValueError:
        print("Ошибка: Несоответствие типа данных. Пожалуйста, введите число.")
