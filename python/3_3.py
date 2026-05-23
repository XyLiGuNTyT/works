from typing import Union, List, Any

def function_name(
    search: str,
    status: bool,
    *args: Any,
    **kwargs: Any
) -> Union[List[int], str]:
    """
    Функция обрабатывает переданные аргументы в зависимости от параметра search.
    Функция может работать с позиционными аргументами (*args) или именованными
    аргументами (**kwargs) и возвращает результат в формате list (список) или str (строка).

    Параметры:
    ----------
    search : str
        Может принимать значения:
        - "args" - работа с позиционными аргументами
        - "kwargs" - работа с именованными аргументами

    status : bool
        Работа с позиционными аргументами args:
        - True - возвращает список целочисленных аргументов из args
        - False - возвращает строку, объединяющую все аргументы args

    *args : Any
        Произвольное количество позиционных аргументов любого типа

    **kwargs : Any
        Произвольное количество именованных аргументов любого типа

    Возвращаемое значение:
    -----------------------
    Union[List[int], str]
        - При search="args" и status=True: список целых чисел из args
        - При search="args" и status=False: строка со всеми значениями args
        - При search="kwargs": строка с перечислением всех ключей и значений kwargs

    Исключения:
    -----------
    ValueError
        Если параметр search не равен "args" или "kwargs"
    """
    result: List[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")