n = input('Ваше имя')
s = input('Ваша фамилия')
age = input('Ваш возраст:')

print('Через format')
print('имя: {}, фамилия: {}, возраст: {}'.format(n,s,age))

print('Через f-strg')
print(f'имя сээр: {n}', f'фамилия: {s}', f'возраст: {age}')