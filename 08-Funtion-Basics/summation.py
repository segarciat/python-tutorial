def partial_sums(f, lower_bound, upper_bound):
    """
    Given a sequence defined by the function f,
    computes the partial sums from lower_bound to upper_bound.

    :param f: A function
    :param lower_bound int: The starting index (included).
    :param upper_bound int: The ending index (included).
    :return: The sum from lower_bound to upper_bound.
    """
    result = 0
    for k in range(lower_bound, upper_bound + 1):
        result += f(k)
        print(f"{k}th value is {result}")

    return result