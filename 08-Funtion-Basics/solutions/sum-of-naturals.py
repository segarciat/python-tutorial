def sum_up_to(n):
    """Computes the sum of the first n natural numbers.

    Args:
        n (_type_): A non-negative integer.

    Returns:
        int: The sum of the first n natural numbers.
    """
    return (n * (n + 1)) // 2

# Should be 15
print(sum_up_to(5))

# should be 78
print(sum_up_to(12))