vvod = input("Введите строку: ")

words = vvod.lower().split()

list = {}

for word in words:
    list[word] = list.get(word, 0) + 1

for word, count in list.items():
    print(f"{word}: {count}")