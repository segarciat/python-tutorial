# Numbers in Python

As we saw previously, Python supports a variety of number types, such
as `int` for integers, `float` for numbers that may have fractionl parts,
and `complex` for complex numbers. There are others, but these shall suffice
for us.

Begin by creating a file `numbers_and_math.py`:

```bash
code numbers_and_math.py
```

## Number Types

Computers make use of memory to keep track of information about running
programs. However, memory is a finite resource, and you may appreciate
this because you likely paid extra money to upgrade the amount of RAM
(Random Access Memory) on your computer, perhaps to have 8GB instead of
4GB.

One consequence of the limitation of memory is that computers have
different representations for different types of numbers. For example,
integers, which are numbers with no fractional part (which may be
positive or negative), can be represented exactly, but typically there
is a limit on the largest integer that can be represented.
On the other hand, numbers with fractional parts cannot have represented
exactly because the finite limitation on memory means that numbers with
infinitely-many digits after the decimal point cannot all be stored in memory.

Python provides the `int` data type for integers, and the `float`
data type for numbers with fractional parts. You will certainly
notice the lack of accuracy and rounding errors related to the `float`
data type while doing numerical calculations. We will not delve deeper
into the issues related to these data types, but being aware of them
can help when the answers you get differ from what you would expect.

## Numeric Literals

A *number literal* is text that appears explicitly in our Python script
such as `0` or `5.2`, and which in turn evaluates to a number. This is
as opposed to numbers that are produced as the results of computations,
but which do not appear explicitly in our Python script.

Here are examples of literals; add them to your script:

```python
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
```

## Arithmetic Operations

Python supports many familiar operations through specific symbols:

- `x + y`: The sum of `x` and `y`.
- `x - y`: The difference of `x` and `y`.
- `x * y`: The product of `x` and `y`.
- `x / y`: The quotient of `x` and y`.
- `x ** y`: `x` to the power of `y`.
- `x // y`: Floor division. That is, the quotient of `x` and `y` discarding the remainder.
Mathematically this yields an integer, but depending on `x` and `y`, it may be an `int`
(such as `7`) or a `float` (such as `7.0`) in Python. Notice this is different from rounding!
- `x % y`: The remainder  of dividing `x` and `y`. Think of finding how many `y`'s fit
into `x`, and taking out those `y`'s from `x`. What remains is `x % y`.
- `x * (y + z)`: Parentheses used for precedence; think PEMDAS from high school algebra.
Normally multiplication has higher precedence than addition, but here we do `y + z` before
multiplying by `x` because of the parentheses.

Type the following in your script:

```python
# Add
print(2 + 3)
# Subtract
print(7.2 - 5)
# Multiply
print(3 * (5 + 7))
# Divide
print(25 / 7)
# Power (Exponent)
print(2 ** 5)
# Power (Exponent), specifically square root
print(4 ** (1/2))

# Floor division
print(25 // 7)

# Remainder, sometimes referred to as modulus
print(25 % 7)
```

You will see:

```text
5
2.2
36
3.5714285714285716
32
5.0
3
4
```

In general, we can use numbers of different data types together in
operations. The data type of the resut generaly depends on the operands.
For example, `25 / 7` evaluates to a `float`, but `25 // 7` evaluates
to an `int`. To see this, add the following to the end of your script:

```python
# float
print(type(25 / 7))
# int
print(type(25 // 7))
```

## Built-In Functions for Math

Python provides many built-in functions. For example we have seen the
built-in `print()` and `type()` functions. The following built-in
mathematical functions are also available:

- `abs(x)`: The absolute value of `x`.
- `pow(x, y)`: `x` to the power of `y`. This is like `x ** y`.
- `round(x)`: Rounds `x` to the nearest integer. We can also
use the form `round(x, ndigits=k)` to round `x` to `k` digits
after the decimal point. In this second form, `ndigits` is
known as a *keyword-argument*, and we will return to this
whne we discuss functions in the future.

There are many built-in functions that can be used for mathematical
computations, which we will discuss in due time.

Add the following to your Python script to see these in action:

```python
print(abs(-1.0))
print(abs(-4))
print(abs(7))
print(abs(0))

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
```

## The `math` module

Python does not have a built-in function for every operation.
However, Python is built to be extended. One way to extend Python
is through modules, which are created by using core Python features.
A **module** is a file containing Python definitions and statements.
For our purposes, a module provides access to other symbols representing
variables and functions.

Of immediate interest is the `math` module, which defines names for
variables and functions that are commonly used. To use the functionality
in a module, we must *import the module* by using the `import` statement
together with the name of the module. A best practice is to place `import`
statements at the very top of a Python script.

Let's briefly start the REPL by running the `python` command in the terminal:

```bash
python
```

```text
sgarciat@fx505gt:~/repos/Python-Tutorial$ python3
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Once it starts up add the following commands:

```text
>>> import math
```

This line imports the `math` module, making the functions
and names in it accessible to us. To learn what's available, we can
use the built-in `help()` function. As its argument, we will provide
`math`, the name of the module we've just imported:

```text
>>> help(math)
```

Here's a truncated version of what I see in my system:

```text
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.

    asin(x, /)
        Return the arc sine (measured in radians) of x.

        The result is between -pi/2 and pi/2.

```

As you can see, Python provides many mathematical functions.
In this view, you can use your arrow keys to scroll up and down
to explore what's available. To exit the paging view due to the
built-in `help()` function, press `q`. Then exit the REPL by entering
`exit()` built-in function:

```text
sgarciat@fx505gt:~/repos/Python-Tutorial$ python3
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> help(math)

>>> exit()
sgarciat@fx505gt:~/repos/Python-Tutorial$
```

Create a new Python script `math_and_random_modules.py`:

```bash
code math_and_random_modules.py
```

Add the following at the top of your script

```python
import math

print(math.gcd(6, 14))
```

We begin with the import statement, `import math`. From here on,
we can access anything it makes available by first adding the
prefix `math.`. That is, the name of the module and a dot `.`.
This use of the dot `.` is known as *dot notation*, and in some
languages `.` is known as the *member access operator*, presumably
because we are accessing members of the object (here the object
would be the `math` module).

For example, we wanted to use the `gcd()` function (which stands
for greatest common divisor), so we wrote `math.gcd()`. This
is a function call like any other, and it accepts integers as
inputs (arguments), which here are `6` and `14`. This produces
the value `2`, which `print()` accepts as its input and displays
onto the screen.

Now towards the end of the file, add the following lines:

```python
# Functions in the math module
print(math.sqrt(2))
print(math.log(1))
print(math.log10(100))
print(math.exp(1))
print(math.factorial(4))
print(math.sin(0))
print(math.cos(0))
print(math.tan(math.PI / 4))
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.lcm(3, 5, 6))
print(math.gcd(3, 5, 6))

# (Constant) variables in the math module
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
```

Notice the syntax is the same for all of these expressions. The last four,
`math.e`, `math.pi`, `math.inf`, and `math.nan`, do not use parentheses
because they are not functions. These are *variables*, the subject of
our next section. This is not an exhaustive list of all that is available
in the `math` module, but you can explore as the need arises.

# The `random` module

Sometimes it is also useful to generate the random numbers. For this,
we can use the `random` module. Of interest for now are two specific
functions:

- `random.randint(min, max)`: Produce a random integer (an `int`) that can be as
small as `min` and as large as `max`. Both `min` and `max` are included.
- `random.random()`: Produces a random `float` at least `0.0` but *less* than `1.0`.
- `random.uniform(a, b)`: Produces a random `float` that is at least `a` and *at most* `b`.

Add the `import` statement at the top of your code:

```python
import random
```

Then add the following lines at the end of your script:

```python
# Produce any integer between -55 and 100 with equal likelihood
print(random.randint(-55, 100))
# Produce any fraction between 0 and 1 with equal likelihood
print(random.random())
# Produce any fraction between 1.0 and 4.5 with equal likelihood
print(random.uniform(1.0, 4.5))
```

We will talk about variables next.

```

## References

- [Built-in Functions in Python](https://docs.python.org/3/library/functions.html#round).
- [Mathematical Functions in Python](https://docs.python.org/3/library/math.html).
