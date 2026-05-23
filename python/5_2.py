import random
import math
import statistics

# Генерируем 100 случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(100)]

# Вычисляем нужные величины
mean = statistics.mean(numbers)                # среднее арифметическое
median = statistics.median(numbers)            # медиана
stdev = statistics.stdev(numbers)              # стандартное отклонение (выборочное)
sum_sqrt = math.sqrt(sum(numbers))             # квадратный корень из суммы

# Округляем до двух десятичных знаков
print(f"Среднее: {mean:.2f}, Медиана: {median:.2f}, Стандартное отклонение: {stdev:.2f}, Корень из суммы: {sum_sqrt:.2f}")