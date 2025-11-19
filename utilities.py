def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def get_max_value(numbers):
    """
    Return the maximum value from an iterable of comparable items.

    Parameters
    ----------
    numbers : iterable
        An iterable (e.g., list or tuple) of comparable values (such as ints or floats).
        If the iterable is empty or falsy, the function returns None.

    Returns
    -------
    Same type as elements or None
        The largest value found in `numbers`, or None if `numbers` is empty.

    Notes
    -----
    - Elements must be mutually comparable using the '>' operator.
    - Runs in O(n) time and uses O(1) additional space.

    Examples
    --------
    >>> get_max_value([1, 4, 2])
    4
    >>> get_max_value([])
    None
    """
    if not numbers:
        return None
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val
