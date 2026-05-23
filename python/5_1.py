import random
import string
from pathlib import Path

def main():
    # Указываем директорию, где будут созданы файлы
    dir_path = Path("random_files")
    # Создаём директорию, если её нет
    dir_path.mkdir(exist_ok=True)

    # Генерируем 10 случайных имён и создаём файлы
    for _ in range(10):
        # Генерируем случайную строку из 8 символов: буквы (верхний/нижний регистр) и цифры
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        # Добавляем расширение .txt
        filename = random_name + ".txt"
        # Полный путь к файлу
        file_path = dir_path / filename
        # Создаём пустой файл
        file_path.touch()

    # Выводим абсолютные пути всех созданных файлов
    for file_path in dir_path.glob("*.txt"):
        print(file_path.resolve())

if __name__ == "__main__":
    main()