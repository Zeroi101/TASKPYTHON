#coding=utf-8
def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)
assert average_num([1, 2, 3, 4]) == 2.5
assert average_num("ABOBA") == "Bad request"
assert average_num(["perviy", "vtoroy"]) == "Bad request"
assert average_num([12]) == 12
assert average_num([-1, -2, -3, -4]) == -2.5
assert average_num([1.5, 2.5]) == 2
assert average_num([0, 0, 0]) == 0
assert average_num([]) == "Bad request"