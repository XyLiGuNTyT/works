while True:
    num = input("Введите число: ")

    if num == 'exit':
        print("Выход из программы...")
        break

    if num.lstrip('-').isdigit() and num != '-':
        digits = len(num) - (1 if num[0] == '-' else 0)
        print(f"В этом числе {digits} цифр.")
    else:
        print("Ошибка: данные не являются числом.")