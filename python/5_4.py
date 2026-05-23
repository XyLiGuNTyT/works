import random
import datetime
import array

def main():
    # Текущая дата
    today = datetime.date.today()
    # Приблизительная дата 5 лет назад (используем 5 * 365 дней)
    start_date = today - datetime.timedelta(days=5 * 365)
    days_range = (today - start_date).days

    # Генерация 10 случайных порядковых номеров дней
    start_ordinal = start_date.toordinal()
    random_ordinals = [start_ordinal + random.randint(0, days_range) for _ in range(10)]

    # Создание массива целых чисел
    dates_array = array.array('i', random_ordinals)

    # Вычисление разницы между соседними датами
    for i in range(len(dates_array) - 1):
        ord1 = dates_array[i]
        ord2 = dates_array[i + 1]
        diff = abs(ord2 - ord1)

        # Преобразование порядковых номеров обратно в даты
        date1 = datetime.date.fromordinal(ord1).strftime("%Y-%m-%d")
        date2 = datetime.date.fromordinal(ord2).strftime("%Y-%m-%d")

        print(f"Разница между {date1} и {date2}: {diff} дней")

if __name__ == "__main__":
    main()