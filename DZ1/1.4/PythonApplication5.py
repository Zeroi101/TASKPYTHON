#coding=windows-1251
def check_shot(shot, ship):
    shot = shot.lower()
    ship = ship.lower()
    
    if shot in ship:
        return "���������!"
    else:
        return "����!"
ship = "�1�1�1 �4�5 �4�5�6�7 �3 �6 �2�2"
user_shot = input("������� ���������� ��������: ")
result = check_shot(user_shot, ship)
print(result)