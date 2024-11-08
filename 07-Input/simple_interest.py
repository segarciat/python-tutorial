print("""
    Welcome to my Simple Interest program!

Please follow the instructions and I will do the interest
computation for you.
""")

# Get the input from the user
principal_input = input("Enter the principal to the nearest dollar: ")
interest_rate_input = input("Enter the yearly interest rate as a percent (1 to 100): ")
number_of_periods_input = input("Enter the number of periods in years: ")

# Convert data from str to appropriate number type
principal = float(principal_input)
yearly_rate = float(interest_rate_input)
years = float(number_of_periods_input)

# Compute and display the result
interest = round(principal) * (yearly_rate / 100) * years
print(f"According to our simple interest rate formula, the interest amout is ${interest:.2f}")