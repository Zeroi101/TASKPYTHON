#coding=windows-1251
while True:
    user_input = input("������� �����:")

    if user_input == 'exit':
        print("��������� ���������.")
        break
    
    try:
        number = int(user_input)
        length = len(str(number))
        print("����� �����:", length)
    except ValueError:
        print("������: �������������� ���� ������. ����������, ������� �����.")
