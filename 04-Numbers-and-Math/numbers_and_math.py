# int literals: the - is used for negative numbers
print(0)
print(5)
print(-7)

# Use underscores for large numbers
print(3_123_459_789)

# float literals, use dots for fractional parts
print(3.14)
# scientific notation
print(1.7e-2)

# complex number literal
print(3-4.5j)

# Addition
print(2 + 3)

# Subtraction
print(7.2 - 5)

# Square root
print(3 * (5 + 7))

# Division
print(21 / 7)

# Exponent (2 to the power of 5)
print(2 ** 5)

# Exponent (25 to the power of 1/2, or square root of 25)
print(25 ** (1/2))

# Divide 21 by 7, and discard the fractional part
print(21 // 7)

# Obtain the remainder of dividing 21 by 7 (think long division)
print(21 % 7)

# The operands are integers, but the value of the expression is of type float
print(type(21 / 7))

# The operands and the resulting value are all of type int
print(type(21 // 7))

# Absolute value function
print(abs(-1.0))
print(abs(-4))
print(abs(7))
print(abs(0))

# Similar to 2 ** 5
print(pow(2, 5))

print(round(3.4))
print(round(3.5))
print(round(3.6))

print(round(3.14159265))
print(round(3.14159265, ndigits=0))
print(round(3.14159265, ndigits=1))
print(round(3.14159265, ndigits=2))
print(round(3.14159265, ndigits=3))
print(round(3.14159265, ndigits=4))