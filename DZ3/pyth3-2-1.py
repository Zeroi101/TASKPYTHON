from typing import List
def multiply_elements(elements: List[int], multiplier: int = 2) -> List[int]:
    return [element * multiplier for element in elements]
elements_input = input("введите числа: ")
elements = [int(x) for x in elements_input.split()]
multiplier_input = int(input("введите множитель: ") or "2")
result = multiply_elements(elements, multiplier_input)
print(result)
