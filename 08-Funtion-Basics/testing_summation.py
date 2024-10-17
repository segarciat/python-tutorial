import math
import summation

def complicated_function(x):
    return 1 / ((1 + x)**3)

summation.partial_sums(complicated_function, 1, 5)

def geometric(k):
    r = 2/3
    return r ** k

summation.partial_sums(geometric, 1, 5)
summation.partial_sums(math.factorial, 1, 5)