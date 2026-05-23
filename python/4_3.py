def append_and_print_even(text, filename):
    # Проверяем, существует ли файл и есть ли в нём что-то
    try:
        # Пытаемся открыть файл для чтения
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        if content:  # если файл не пустой
            need_newline = True
        else:
            need_newline = False
    except FileNotFoundError:
        # файл ещё не существует – значит, он пустой (новый)
        need_newline = False

    # Теперь открываем файл для добавления (режим 'a')
    with open(filename, 'a', encoding='utf-8') as f:
        if need_newline:
            f.write('\n')      # сначала переводим строку
        f.write(text)          # потом пишем сам текст

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()           # читаем все строки в список
        # enumerate нумерует строки, начиная с 1 (первая строка – номер 1)
        for i, line in enumerate(lines, start=1):
            if i % 2 == 0:               # если номер чётный выводим
                print(line.rstrip('\n'))

append_and_print_even("rtx 2050", "rab.txt")
append_and_print_even("rtx 3050", "rab.txt")
append_and_print_even("rxt 4060", "rab.txt")
append_and_print_even("rtx 4090", "rab.txt")
append_and_print_even("rx 6600", "rab.txt")
