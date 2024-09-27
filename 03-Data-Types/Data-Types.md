# Data Types

Armed with `print()`, we can explore what Python has to offer.
Before we do that, we briefly mention data types. In Python, expressions
have a **data type**, which determines what operations are allowed on the
corresponding values, and what they do. For example, Python distinguishes
between integers, fractions, complex numbers, text, lists of items, and more.

A useful Python built-in function to explore this is the `type()` function.
The `type()` function accepts an expression as its argument, and it
displays the type (its "class").

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

In short:

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
