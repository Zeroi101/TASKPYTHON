text = input("текст:")
dct = {}

for abibovba in text:
    if abibovba != ' ':  
        abibovba = abibovba.lower()  
        if abibovba in dct:
            dct[abibovba] += 1
        else:
            dct[abibovba] = 1

print(dct)
