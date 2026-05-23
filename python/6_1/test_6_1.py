from function import average_num   # импорт функции из соседнего файла

def test_integers():
    assert average_num([1, 2, 3, 4]) == 2.5

def test_floats():
    assert average_num([2.5, 3.5]) == 3.0

def test_string_numbers():
    assert average_num(["1", "2", "3"]) == 2.0

def test_mixed_types():
    assert average_num([1, "2", 3.5]) == 2.17

def test_single_element():
    assert average_num([5]) == 5.0

def test_negative_numbers():
    assert average_num([-1, -2, -3]) == -2.0

def test_large_numbers():
    assert average_num([1000, 2000, 3000]) == 2000.0

def test_rounding():
    assert average_num([1, 1, 1, 10]) == 3.25

def test_invalid_string():
    assert average_num([1, "abc"]) == "Bad request"

def test_empty_string():
    assert average_num([""]) == "Bad request"
