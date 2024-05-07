import random
def get_two_random_elements(input_list):
    if len(input_list) < 2:
        return "минимум два элемента в списке"
    random_elements = random.sample(input_list, 2)
    return random_elements
list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
result = get_two_random_elements(list_el)
print(result)
