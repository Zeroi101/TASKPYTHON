#coding=windows-1251
while True:
    user_input = input("Введите число: ")

    if user_input == 'exit':
        print("Программа завершена.")
        break
    
    try:
        number = int(user_input)
        
        print("Числа в интервале [-{}, {}]:".format(number, number + 1))
        negative_sum = 0
        positive_sum = 0
        for i in range(-number, number + 1):
            print(i, end=" ")
            if i < 0:
                negative_sum += i
            elif i > 0:
                positive_sum += i
       
        print("\nСумма отрицательных чисел:", negative_sum)
        print("Сумма положительных чисел:", positive_sum)
        
    except ValueError:
        print("Ошибка: Несоответствие типа данных. Пожалуйста, введите число.")