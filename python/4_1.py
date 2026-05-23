import math
# 1. Список квадратов первых 10 натуральных чисел
squares = [x**2 for x in range(1, 11)]
print("1.", squares)

# 2. Словарь дней недели
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_dict = {day: i+1 for i, day in enumerate(days)}
print("2.", day_dict)

# 3. Множество тегов в нижнем регистре
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_lower = {tag.lower() for tag in tags}
print("3.", tags_lower)

# 4. Четные числа из списка
numbers = [1, 3, 4, 87, 98, 15, 7, 4, 66]
evens = [x for x in numbers if x % 2 == 0]
print("4.", evens)

# 5. Словарь факториалов
factorials = {n: math.factorial(n) for n in range(1, 6)}
print("5.", factorials)