import math
import random

# Special numbers: infinity, -infinity, and nan
print(float('inf'))
print(float('-inf'))
print(float('nan'))

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

# pi = 3.14159...
print(math.pi)

# e = Euler's number = 2.718...
print(math.e)

# Infinity (type is float)
print(math.inf)

# Not a Number (type is float)
print(math.nan)

# Square root of 2
print(math.sqrt(2))

# ln (natural logarithm) a.k.a. log base e
print(math.log(1))

# log base 10
print(math.log10(100))

# exponential function, e to the x
print(math.exp(1))

# 4! meaning 4 factorial
print(math.factorial(4))

# trigonometric function: sine
print(math.sin(0))

# trigonometric function: cosine
print(math.cos(0))

# trigonometric function: tangent
print(math.tan(math.pi / 4))

# trigonometric function: arcsin (a.k.a. inverse sine)
print(math.asin(1))

# trigonometric fucntion: arccos (a.k.a. inverse cosine)
print(math.acos(1))

# trigonometric function: arctan (a.k.a. inverse tangent)
print(math.atan(1))

# least common multiple of 3, 5, and 6
print(math.lcm(3, 5, 6))

# greatest common divisor of 3, 5, and 6
print(math.gcd(3, 5, 6))

# ceiling function: smallest integer greater than 3.5 (compare to rounding)
print(math.ceil(3.4))

# floor function: largest integer smaller than 3.5
print(math.floor(3.5))

print(random.randint(-55, 100))
print(random.random())
print(random.uniform(1.0, 4.5))