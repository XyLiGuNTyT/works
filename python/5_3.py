import random
import json
import string

def generate_user():
    # Список возможных имён для разнообразия
    first_names = ["Иван", "Петр", "Анна", "Мария", "Егор", "Владимир", "Алексей", "Ольга"]
    last_names = ["Иванов", "Петров", "Сидорова", "Кузнецов", "Петрова", "Иванова", "Попов", "Васильева"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"

    age = random.randint(18, 30)

    # Генерация email: случайное имя + случайное число + @example.com
    email_local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    email = f"{email_local}@gmail.com"

    # Генерация пароля: 12 символов из букв (верхний и нижний), цифр и знаков препинания
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_chars, k=12))

    return {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }

# Генерация пользователя
user_data = generate_user()

# Сохранение в JSON-файл
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=4)

# Чтение из файла и вывод
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(json.dumps(loaded_data, ensure_ascii=False, indent=4))