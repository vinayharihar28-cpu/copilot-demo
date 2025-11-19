def is_even(n):
    """
    Check if a number is even.
    
    Args:
        n: An integer to check
        
    Returns:
        True if the number is even, False otherwise
    """
    return n % 2 == 0


def process_numbers(numbers):
    """
    Process a list of numbers and return useful statistics.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        A dictionary containing:
        - sum: Total of all numbers
        - average: Mean of the numbers
        - max: Maximum value
        - min: Minimum value
        - count: Total count of numbers
    """
    if not numbers:
        return {
            'sum': 0,
            'average': 0,
            'max': None,
            'min': None,
            'count': 0
        }
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        'sum': total,
        'average': average,
        'max': maximum,
        'min': minimum,
        'count': count
    }


# Example usage
if __name__ == "__main__":
    # Test is_even function
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Testing is_even function:")
    for num in test_numbers:
        print(f"{num} is even: {is_even(num)}")
    
    # Test process_numbers function
    print("\nTesting process_numbers function:")
    sample_numbers = [10, 25, 30, 45, 50, 15, 20]
    result = process_numbers(sample_numbers)
    
    print(f"Numbers: {sample_numbers}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
    print(f"Max: {result['max']}")
    print(f"Min: {result['min']}")
    print(f"Count: {result['count']}")