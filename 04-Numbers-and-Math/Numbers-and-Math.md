# Numbers in Python

As we saw previously, Python supports a variety of number types, such
as `int` for integers, `float` for numbers that may have fractionl parts,
and `complex` for complex numbers. There are others, but these shall suffice
for us.

Begin by creating a file `numbers_and_math.py`:

```bash
code numbers_and_math.py
```

## Numeric Literals

A *number literal* is text that appears explicitly in our Python script
such as `0` or `5.2`, and which in turn evaluates to a number. This is
as opposed to numbers that are produced as the results of computations,
but which do not appear explicitly in our Python script. We will meet
literals for other data types in due time.

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

## Arithmetic Operations

Python supports many familiar operations through specific symbols:

- `x + y`: The sum of `x` and `y`.
- `x - y`: The different of `x` and `y`.
- `x * y`: The product of `x` and `y`.
- `x / y`: The quotient of `x` and y`.
- `x ** y`: `x` to the power of `y`.
- `x // y`: The quotient of `x` and `y` discarding the remainder. Mathematically this yields an
integer, but depending on `x` and `y`, it may be an `int` (such as `7`) or a `float` (such as `7.0`)
in Python.
- `x % y`: The remainder  of dividing `x` and `y`.
- `x * (y + z)`: Parentheses used for precedence; think PEMDAS from high school algebra.
Normally multiplication has higher precedence than addition, but here we do `y + z` before
multiplying by `x`.

Type the following:

```python
print(2 + 3)
print(7.2 - 5)
print(3 * (5 + 7))
print(21 / 7)
print(2 ** 5)
print(4 ** (1/2)) # square root
print(21 // 7)
print(21 % 7)
```

You will see:

```text
5
2.2
36
3.0
32
5.0
3
0
```

In general, we can use numbers of different data types together in
operations. The data type of the resut generaly depends on the operands.
For example, `21 / 7` evaluates to a `float`, but `21 // 7` evaluates
to an `int`. To see this, add the following to the end of your script:

```python
print(type(21 / 7))
print(type(21 // 7))
```

## Built-In Functions for Math

Besides the operators we have seen, Python also provides some built-in functions
for familiar computations:

- `abs(x)`: Absolute value of `x`.
- `pow(x, y)`: `x` to the power of `y`. This is like `x ** y`.
- `round(x, ndigits=k)`: Round the nubmer `x` to `k` digits after the decimal point.
Alternatively, `round(x)` will round to the nearest integer.

There are other built-in functions that are relevant to mathematical operations,
such as `sum()` to find the sum of a list of numbers, `max()` to find the maximum
value of a list of numbers, `min()` to find the minimum value of a list of numbers,
and others. We will discuss these when we talk about data types used to hold
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

## The `math` module and the `random` modules

There are many other mathematical operations, but they do not exist as
built-in functions. Instead, we ensure using *modules* (sometimes referred
to as *library* or *package*)l, which provide extra functionality. For example,
Python provides the `math` module defining trigonometric functions, exponential
functions, logarithms, and more.

To use the functionality in a module, we must *import the module* by using
the `import` statement. A best practice is to place `import` statements at
the very top of the Python script.

Modify your script so that the very first line is as follows:

```python
import math
```

Now towards the end of the file, add the following lines:

```python
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
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
```

Notice that for each symbol provided by the `math` module, we must prepend
`math.`. This is called *dot notation*, and it is a syntax used to access
attributes and methods (variables and functions) in some other object,
in this case the `math` module.

Sometimes it is also useful to generate the random numbers. For this,
we can use the `random` module. Of interest for now are two specific
functions:

- `random.randint(min, max)`: Produce a random integer (an `int`) that can be as
small as `min` and as larg as `max`.
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

## References

- [Built-in Functions in Python](https://docs.python.org/3/library/functions.html#round).
- [Mathematical Functions in Python](https://docs.python.org/3/library/math.html).
