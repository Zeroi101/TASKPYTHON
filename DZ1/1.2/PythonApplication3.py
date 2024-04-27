#coding=windows-1251
while True:
    user_input = input("������� �����: ")

    if user_input == 'exit':
        print("��������� ���������.")
        break
    
    try:
        number = int(user_input)
        
        print("����� � ��������� [-{}, {}]:".format(number, number + 1))
        negative_sum = 0
        positive_sum = 0
        for i in range(-number, number + 1):
            print(i, end=" ")
            if i < 0:
                negative_sum += i
            elif i > 0:
                positive_sum += i
       
        print("\n����� ������������� �����:", negative_sum)
        print("����� ������������� �����:", positive_sum)
        
    except ValueError:
        print("������: �������������� ���� ������. ����������, ������� �����.")