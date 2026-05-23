dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys = set(dct.keys())
znach = set(dct.values())

union_set = keys | znach

print("Множество ключей:", keys)
print("Множество значений:", znach)
print("Объединение:", union_set)