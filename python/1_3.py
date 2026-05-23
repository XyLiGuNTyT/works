u_input = input('Введите ваш возраст:')

try:
    number = int(u_input)
    if number > 0:
        if number > 17:
            print(f'Вы совершеннолетний!')
        else:
            print(f'Вы несовершеннолетинй')
    else:
        print('Ошибка: Возвраст не может быть отрицательным!!!')

except ValueError:
    print('Ошибка: Введено не число')