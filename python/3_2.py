import math
# 1. Сложение
def add(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Слагаемые должны быть числами")
    return a + b

# 2. Вычитание
def subtract(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a - b

# 3. Умножение
def multiply(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a * b

# 4. Деление
def divide(a: float, b: float, mode: str) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено")

    if mode == "/":
        return a / b
    elif mode == "//":
        return a // b
    elif mode == "%":
        return a % b
    else:
        raise ValueError("Неверный режим деления")

# 5. Возведение в степень
def power(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами")
    return a ** b

# 6. Факториал
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Факториал можно вычислить только для целого числа")
    if n < 0:
        raise ValueError("Факториал отрицательного числа невозможен")
    return math.factorial(n)

# 7. Синус
def sine(x: float) -> float:
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    return math.sin(x)

# 8. Медиана
def median(numbers: list[float]) -> float:
    if not isinstance(numbers, list):
        raise TypeError("Нужен список чисел")
    if len(numbers) == 0:
        raise ValueError("Список пуст")

    numbers = sorted(numbers)
    n = len(numbers)

    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

# Список действий калькулятора
while True:
    print("""
Доступные операции:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Возведение в степень
6. Факториал
7. Синус
8. Медиана
""")

    operation = input("Операция (или exit): ")

    if operation.lower() == "exit":
        break

    try:
        if operation == "1":
            a = float(input("Слагаемое 1: "))
            b = float(input("Слагаемое 2: "))
            print(">>>", add(a, b))

        elif operation == "2":
            a = float(input("Уменьшаемое: "))
            b = float(input("Вычитаемое: "))
            print(">>>", subtract(a, b))

        elif operation == "3":
            a = float(input("Множитель 1: "))
            b = float(input("Множитель 2: "))
            print(">>>", multiply(a, b))

        elif operation == "4":
            a = float(input("Делимое: "))
            b = float(input("Делитель: "))
            mode = input("Тип деления (/ // %): ")
            print(">>>", divide(a, b, mode))

        elif operation == "5":
            a = float(input("Основание: "))
            b = float(input("Степень: "))
            print(">>>", power(a, b))

        elif operation == "6":
            n = int(input("Число: "))
            print(">>>", factorial(n))

        elif operation == "7":
            x = float(input("Угол (в радианах): "))
            print(">>>", sine(x))

        elif operation == "8":
            nums = list(map(float, input("Список чисел: ").split()))
            print(">>>", median(nums))

        else:
            print("Неизвестная операция")

    except Exception as e:
        print("Ошибка:", e)

    print("--------------------")