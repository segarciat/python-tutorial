value_entered_by_user = input("Please enter a number: ")
print(f"You entered: {value_entered_by_user}, and it has type {type(value_entered_by_user)}")

more_user_input = input("Enter anything else: ")
print(f"You entered {more_user_input}, and it has type {type(more_user_input)}")

four_as_a_string = '-4'
four = int(four_as_a_string)
print(f"The type of {four_as_a_string=} is {type(four_as_a_string)}")
print(f"The type of {four=} is {type(four)}")

pi_as_a_string = '3.14'
my_pi = float(pi_as_a_string)
print(f"The type of {pi_as_a_string=} is {type(pi_as_a_string)}")
print(f"The type of {my_pi=} is {type(my_pi)}")