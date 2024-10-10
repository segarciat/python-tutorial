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
On the other hand, typical representations of number with fractional
parts cannot have represented exactly because the finite limitation on memory
means that numbers with infinitely-many digits after the decimal point
cannot all be stored in memory.

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
but which do not appear explicitly in our Python script. We will meet
literals for other data types in due time.

## Arithmetic Operations

Python supports many familiar operations through specific symbols:

- `x + y`: The sum of `x` and `y`.
- `x - y`: The different of `x` and `y`.
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
multiplying by `x`.

Type the following:

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

Besides the operators we have seen, Python also provides some built-in functions
for familiar computations:

- `abs(x)`: Absolute value of `x`.
- `pow(x, y)`: `x` to the power of `y`. This is like `x ** y`.
- `round(x, ndigits=k)`: Round the nubmer `x` to `k` digits after the decimal point.
Alternatively, `round(x)` will round to the nearest integer.

Remember that to call a function, you include the name, parentheses, and the
arguments, possibly separated by commas. In this case of `round()`, the
`ndigits` is something called a *keyword-argument*, which we will discuss
later. The `ndigits` keyword argument is specific to `round()`, and
though we will not discuss keyword-arguments right now, its usage
is simple enough, so you are encouraged to use it.

There are other built-in functions that are relevant to mathematical operations,
such as

- `sum()`: find the sum of a list of numbers,
- `max()`: find the maximum value of a list of numbers,
- `min()` to find the minimum value of a list of numbers, and others.

We will discuss these when we talk about data types used to hold
more than one value, such as `list`, `set`, and `tuple`.

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

Python does not have a built-in for every operations. However,
its functionality can be extended through *modules*. A **module**
is a file containing Python definitions and statements. For our
purposes, a module provides access to other symbols representing
variables and functions.

One useful module related to numerics is the `math` module.
To use the functionality in a module, we must *import the module* by using
the `import` statement together with the name of the module.
A best practice is to place `import` statements at
the very top of a Python script.

Let's briefly start the REPL by running the `python` command in the terminal:

```bash
python
```

Once it starts up add the following commands:

```text
sgarciat@fx505gt:~/repos/Python-Tutorial$ python3
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> help(math)
```

Here's a truncated version of the output on my system:

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
To exit the paging view due to the built-in `help()` function,
press `q`. Then exit the REPL by entering `exit()` built-in function:

```text
sgarciat@fx505gt:~/repos/Python-Tutorial$ python3
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> help(math)

>>> exit()
sgarciat@fx505gt:~/repos/Python-Tutorial$
```

To use a function in a module, such as `math`, such as `acos()`,
we write the following:

```text
math.acos(0)
```

There command has the following components:

- We begin with the module name: `math`.
- We append a dot `.` to the module name, like so: `math.`. The
dot is known as the *dot operator*, and it is used to access names
and attributes of an object. In this case, the object is the math
module. We will see the dot operator in other contexts in the future.
- We write the name of the symbol we wish to access. In this case,
the symbol is the function `acos()`. Since the function expects an
argument, I pass it `0` (which is in the domain of arc cosine).

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
our next section.

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
print(random.randint(-55, 100))
print(random.random())
print(random.uniform(1.0, 4.5))
```

We will talk about variables next.

## Special Values: infinity and NaN

Python can represent infinity and negative infinity but there isn't a
literal for it. Instead, we must use the `float()` function, like so:

```python
print(float('inf'))
print(float('-inf'))
```

Similarly, Python has a special symbol for when something is not a number,
which is typically refererd to as NaN:

```python
print(float('nan'))
```

## References

- [Built-in Functions in Python](https://docs.python.org/3/library/functions.html#round).
- [Mathematical Functions in Python](https://docs.python.org/3/library/math.html).
