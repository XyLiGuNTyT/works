vvod = input("Введите числа через пробел: ").split()
power = int(input("Введите степень: "))

resultat = []
for item in vvod:
    if item.lstrip('-').isdigit():
        num = int(item)
        resultat.append(str(num ** power))
    else:
        resultat.append(item * power)

print("Вывод:", " ".join(resultat))