u_input = input('Ввод числа:')

try:
    number = int(u_input)

    if number < 0:
        print('Error')
    else:
        if number % 2 == 0:
            print(f'Chislo {number} четное')
        else:
            print(f'Chislo {number} не четное')

except ValueError:
    print("Error: Введено не число;")