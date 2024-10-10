def average(x, y):
    """
    Computes the average of two numbers.

    :param float x: Any number.
    :param float y: Any number.
    :return: The average of the inputs.
    """
    return (x + y) / 2

x_input = input("Enter a number: ")
y_input = input("Enter another number: ")

x = float(x_input)
y = float(y_input)

average_of_xy = average(x, y)

print(f"The average of {x} and {y} is {average_of_xy}.")
