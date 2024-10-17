# An import statement is needed to access functions and variables in a module
import math
import random


# To access names in a module, we prefix with the module name and a dot
print(math.gcd(6, 14))

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

# Produce any integer between -55 and 100 with equal likelihood
print(random.randint(-55, 100))
# Produce any fraction between 0 and 1 with equal likelihood
print(random.random())
# Produce any fraction between 1.0 and 4.5 with equal likelihood
print(random.uniform(1.0, 4.5))