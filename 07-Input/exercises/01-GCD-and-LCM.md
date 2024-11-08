# 1. Practice: GCD and LCM

Create a program `gcd_and_lcm.py` that prompts a user for two
integers and displays: their product, their greatest common divisor,
their least common multiple, and the product of their greatest common
divisor and their least common multiple. Be sure your output message
is a complete sentence, so that your user knows what each
value represents.

Here are some tips:

1. You may assume that your user provides valid integers
as input. Of course, if they don't, your program will
not work, but we will learn how to handle that in the future.

2. Use the `input()` function to get the information from
the user. What is the data type of the value produced by
`input()`?

3. Use the `math.gcd()` and `math.lcm()` functions in the
`math` module to compute the gcd and lcm. What data type
does it expect from its inputs? Do we need to do something
to the value from `input()` beforehand?