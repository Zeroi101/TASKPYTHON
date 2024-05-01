multiply_lambda = lambda elements, multiplier=2: [element * multiplier for element in elements]
elements_input = input("введите числа: ")
elements = [int(x) for x in elements_input.split()]

multiplier_input = int(input("введите множитель: ") or "2")

result_lambda = multiply_lambda(elements, multiplier_input)
print(result_lambda)
