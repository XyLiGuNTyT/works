def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    Игнорирует регистр, пробелы и знаки препинания.
    """
    # Оставляем только буквы и цифры, приводим к нижнему регистру
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]