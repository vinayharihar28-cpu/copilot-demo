# AFTER: Reusable function for multiplying lists

def multiply_list(numbers, factor):
    """Return a new list with each element multiplied by factor."""
    return [n * factor for n in numbers]

numbers = [1, 2, 3, 4, 5]

doubled_numbers = multiply_list(numbers, 2)
tripled_numbers = multiply_list(numbers, 3)
quadrupled_numbers = multiply_list(numbers, 4)

print(doubled_numbers)
print(tripled_numbers)
print(quadrupled_numbers)
