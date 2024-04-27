#coding=windows-1251
def check_shot(shot, ship):
    shot = shot.lower()
    ship = ship.lower()
    
    if shot in ship:
        return "Попадание!"
    else:
        return "Мимо!"
ship = "б1в1г1 е4е5 в4в5в6в7 д3 д6 з2к2"
user_shot = input("Введите координаты выстрела: ")
result = check_shot(user_shot, ship)
print(result)