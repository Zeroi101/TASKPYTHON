import re
def check_date_format(date):
    pattern = r"\b\d{4}-\d{2}\b"
    if re.match(pattern, date):
        return True
    else:
        return False
def check_phone_number(phone_number):
    pattern = r"^(?:\+7|7|8)[0-9]{10}$"
    if re.match(pattern, phone_number):
        return True
    else:
        return False
date_to_check = "2004-02"
phone_number_to_check = "+79228133711"
is_date_valid = check_date_format(date_to_check)
is_phone_valid = check_phone_number(phone_number_to_check)
print("формат даты верный:", is_date_valid)
print("номер телефона верный:", is_phone_valid)
