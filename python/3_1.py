def multiply_list(numbers: list[int], multiplier: int = 2) -> list[int]:
    return [num * multiplier for num in numbers]

multiply_list_lambda = lambda numbers, multiplier=2: list(
    map(lambda x: x * multiplier, numbers)
)

numbers_input = input("Введите список чисел через пробел: ")
numbers = list(map(int, numbers_input.split()))

multiplier_input = input("Введите множитель (по умолчанию 2): ")

if multiplier_input.strip() == "":
    multiplier = 2
else:
    multiplier = int(multiplier_input)

result_function = multiply_list(numbers, multiplier)
result_lambda = multiply_list_lambda(numbers, multiplier)

print("Результат (функция):", result_function)
print("Результат (лямбда-функция):", result_lambda)