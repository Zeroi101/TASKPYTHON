dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dct.keys())
values_set = set(dct.values())

merged_set = keys_set.union(values_set)

print("ключи:", keys_set)
print("значения:", values_set)
print("объединенное:", merged_set)

