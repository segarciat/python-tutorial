import random

def generate_lucky_number(smallest, largest):
    """
    Displays a random number in the range defined by the user.

    :param str smallest: The smallest number in the range (included).
    :param str highest:  The largest number in the range (included).
    """
    lucky_number = random.randint(smallest, largest)
    print(f"Drum roll... your lucky number is: {lucky_number}.")


small_number_input = input("Enter an integer: ")
large_number_input = input("Enter a bigger integer: ")

minimum = int(small_number_input)
maximum = int(large_number_input)

# Generate lucky numbers.
print(f"Generating lucky numbers between {minimum} and {maximum}...")

generate_lucky_number(minimum, maximum)
generate_lucky_number(minimum, maximum)
generate_lucky_number(minimum, maximum)
generate_lucky_number(smallest=minimum, largest=maximum)
generate_lucky_number(largest=maximum, smallest=minimum)
generate_lucky_number(minimum, largest=maximum)