import math

# Discriminant and quadratic formula
a = 1
b = 7
c =  10

discriminant = (b ** 2) - 4  * a * c

# We will need to take the square root for both roots,
# so it helps to do the computation once.
discriminant_sqrt = math.sqrt(discriminant)

x_plus  = (-b + discriminant_sqrt) / (2 * a)
x_minus = (-b - discriminant_sqrt) / (2 * a)
print(x_plus)
print(x_minus)
