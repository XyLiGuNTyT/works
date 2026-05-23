from function import is_palindrome

def test_palindrome_phrase():
    assert is_palindrome("А роза упала на лапу Азора") == True

def test_palindrome_with_yo():
    assert is_palindrome("Лёша на полке клопа нашёл") == True

def test_not_palindrome():
    assert is_palindrome("Hello world") == False

def test_numbers():
    assert is_palindrome("12321") == True

def test_empty_string():
    assert is_palindrome("") == True

print("Все 5 тестов пройдены успешно!")