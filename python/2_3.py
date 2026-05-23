list1 = input("Введите первый список: ").split()
list2 = input("Введите второй список: ").split()

set1 = set(int(x) for x in list1)
set2 = set(int(x) for x in list2)

peresech = set1 & set2 or set1.intersection(set2)

if peresech:
    print("Общие элементы:", *peresech)
else:
    print("Общие элементы: отсутствуют")