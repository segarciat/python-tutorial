import math

print("Welcome to my greatest common divisor program")

m_input = input("Enter a positive integer: ")
n_input = input("Enter another positive integer: ")

m = int(m_input)
n = int(n_input)

print(f"The greast common divisor of {m=} and {n=} is {math.gcd(m, n)}")