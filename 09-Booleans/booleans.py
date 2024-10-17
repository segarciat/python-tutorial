# Boolean literals are of type bool
print(True)
print(False)
print(type(True))
print(type(False))

# True
print(1 < 7)
# False
print(-5 > 0)

# True
print(2 >= 2)

# True: apple sorts before orange alphabetically
print("apple" < "orange")

# False: lowercase a comes after uppercase O
print("apple" < "Orange")

# True: notice this is double equal sign, not single equal (assignment)
print(1 == (6 - 5))
# True
print(0 != (-3 - 3))
# False: first letters have different case
print("apple" == "Apple")

# True: the result for or is True when at least one Boolean subexpression is True
print(5 < 0 or 5 > 0)

# False: Both expression must be True for their conjunction to be True
print(5 < 0 and 5 > 0)

# False: The remainder of dividing 5 by 2 is 1, not 0.
print((5 % 2) == 0)

def is_even(n):
    """Determines whether the input integer is even.

    Args:
        n int: An integer

    Returns:
        bool: True if n is even, and False otherwise.
    """
    return (n % 2) == 0

# False
print(is_even(5))

list_of_numbers = [3, 5, 7]
set_of_strings = {"apple", "orange", "strawberry"}
tuple_of_coordinates = (1.5, -3.8)

# True: The value 7 is in the list
print(7 in list_of_numbers)

# False: "kiwi" is not in the set
print("kiwi" in set_of_strings)

# True: 0 is not in the tuple
print(0 not in tuple_of_coordinates)

list_of_numbers = [3, 5, 7]
set_of_strings = {"apple", "orange", "strawberry"}
tuple_of_coordinates = (1.5, -3.8)
dictionary_with_contacts = { "sergio": "sergio@email.com", "peggy": "peggy@email.com" }

# True: The value 7 is in the list
print(7 in list_of_numbers)

# False: "kiwi" is not in the set
print("kiwi" in set_of_strings)

# True: 0 is not in the tuple
print(0 not in tuple_of_coordinates)

# True: "sergio" is a key in the dictionary
print("sergio" in dictionary_with_contacts)