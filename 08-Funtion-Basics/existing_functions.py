import random

# No arguments, produces a float as return value
r = random.random()

# One string argument, produces an int as a return value
five = int('5')

# One integer argument, one float argument, produces None as a return value, and a side effect
print(five, r)

# None is a literal, and no other value has the same type as None
my_none_variable = None
print(f"{my_none_variable=} has type {type(my_none_variable)}")

# We can store the return value of print(), which is None, but this is not usually done
return_value_of_print = print("Hello")
print(f"The print() function returned: {return_value_of_print}")
