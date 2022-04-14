def get_digit(number: int, position: int) -> int:
    """
    Get a digit at a particular postition

    >>> get_digit(234, 0)
    4
    >>> 3 == 4
    False
    >>> [1,2,3,4,5][:3]
    [1, 2, 3]
    >>> "hello"
    'hello'
    >>> x # doctest: +_IGNORE_EXCEPTION_DETAIL
    Traceback to most recent call back
        ...
    NameError:

    """
    return number // (10 ** position) % 10

print(get_digit(234, 0))




