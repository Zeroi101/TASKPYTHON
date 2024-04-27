#coding=windows-1251
def check_number(num):
    num_str = str(num)
    if len(num_str) != 3:
        print("Ошибка: Введите трехзначное число!")
        return False
    
    if len(set(num_str)) < len(num_str):
        print("Ошибка: Число содержит повторяющиеся цифры!")
        return False
    
    return True

def generate_permutations(num):
    if not check_number(num):
        return
    
    num_str = str(num)
    permutations = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and k != i:
                    perm = int(num_str[i] + num_str[j] + num_str[k])
                    permutations.append(perm)
    print("Перестановки числа", num, ":", permutations)
    
while True:
    number = int(input("Введите трехзначное число: "))
    generate_permutations(number)