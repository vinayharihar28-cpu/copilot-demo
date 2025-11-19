def max_in_list(values):
    """Return the maximum value in a list, or None if the list is empty.

    Returns None if the list is empty.
    """
    if not values:
        return None
    max_val = values[0]
    for v in values[1:]:
        if v > max_val:
            max_val = v
    return max_val