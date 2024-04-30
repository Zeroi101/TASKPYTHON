numbers = []
exponent = int(input("Введите степень: "))
num_count = int(input("Введите кол-во чисел в списке: "))

for i in range(num_count):
    num = input("Введите число, которое нужно возвести в степень: ")
    numbers.append(num)


for num in numbers:
    if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):  
        num = float(num)  
        powered_num = num ** exponent
        print(f"{num} в степени {exponent} = {powered_num}")
    else:
        print(f"{num} * {exponent} =", num * exponent)  