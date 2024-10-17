# Data Types

Equipped with `print()`, we can visually explore what Python has to offer.
Before we do that, let's briefly talk about data types. In Python, expressions
have a **data type** or **class**, which determines what operations are allowed
involving their values. For example, Python distinguishes between integers, fractions,
complex numbers, text, lists of items, and more. We will explore these all in due time.

Python provides the built-in function, `type()` which accepts an expression
as its argument, and produces its *class*, which is its *data type*, as its
output. We can provide the output of `type()` as an input to `print()`
to see the class of different expressions (this is like function composition
in algebra).

Create a script called `data_types.py`:

```bash
code data_types.py
```

Type the following:

```python
print(type(0))
print(type(-52))
print(type(1 + 17))
print(type(102 - 255))
print(type(38 * (-48)))
print(type(5.2 / 3.1))
print(type(4 + 8j))
print(type("hello"))
print(type(False))
print(type([5, 7, 0, -2, 23]))
```

You will see:

```text
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'bool'>
<class 'list'>
```

Let's consider how Python handled `print(type(0))`:

1. Python sees `print()` and its argument is `type(0)`, so it begins
by evaluating the argument `type(0)`.

2. Python notes that `type()` is a built-in function with `0` as an argument,
and it invokes that function to produce the type of `0` as a result.
The evaluation of `type(0)` is now complete.

3. Python provides the value  of `type(0)` as an input to `print()`,
which in turn displays the output to the screen. Thus we see
`<class 'int'>`.

Let's briefly go through the types:

- `int` repersents an integer, a number with no fractional part which may be
positive, negative, or zero.
- `float` represents a number that may have a fractional part, like `5.2`.
- `complex` represents a complex number. In Python, complex numbers use the
letter `j` (common in fields like electrical engineering) instead of the `i`
you may be used to from high school algebra.
- `str` represents a *string*, a data type used to represent textual information.
- `bool` represents *boolean*, which is used for a value that may be `True` or `False`.
- `list` is a type of collection used to hold many different values together.

We will explore all of these in due time. The important thing is to be aware of their
existence, and that the types affect what operations you can perform with them.
For example, it's meaningless to "divide" strings; typically, we divide numbers.
We will next talk about numbers.
