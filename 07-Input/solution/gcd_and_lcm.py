import math

print("""
    Welcome to my GCD and LCM program!
Please provide two integers when prompted.
""")

# Get inputs from the user: the results are of type str
m_input = input("Enter the first integer: ")
n_input = input("Enter the second integer: ")

# Convert each str to an int
m = int(m_input)
n = int(n_input)

lcm_mn = math.lcm(m, n)
gcd_mn = math.gcd(m, n)

# Compute and display results
print(f"The least common multiple of {m} and {n} is {lcm_mn}")
print(f"The greaest common divisor of {m} and {n} is {gcd_mn}")
print(f"The product of their gcd and lcm is {lcm_mn * gcd_mn}")
print(f"The product of {m} and {n} is {m * n}")
