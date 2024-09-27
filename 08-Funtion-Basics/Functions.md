# Functions (Basics)

In computer programming, a **function** is a unit of code that has
a name and performs one specific job. Functions provide a way to
hide the complexity of possibly laborious computations behind a
simple-to-use interface. This is known as *abstraction*. For example,
you can use a microwave without knowing the physics of how it works.

## Types of Functions

In Python, functions come in many flavors:

- **Built-in functions**: These ship with Python and have special
language support. Examples: `print()`, `input()`, `len()`, `type()`.

- **Standard Library Functions**: These also ship with Python, but
may require the use of an `import` statement. For example, if we
have `import math` at the top of our script, we can use `math.cos()`
and `math.gcd()` from the `math` module. In this case, we use dot
notation.

- **Methods**: These are functions we can use on objects we have
using the dot notation. So far, we've seen string methods, such
as `myvariable.upper()`, `myvariable.title()`, assuming that
`myvariable` is a string.

- **User-defined functions**: These are functions that we can create
ourselves using the `def` keyword.

- **Functions from other packages**: Sometimes we need functionality
beyond what ships with Python. In this case, we can install a package
such as `numpy`, or `scipy`, or `pygame`, and use functions that they
provide, written by other programmers. We will investigate this much
later.

Our focus in this section is user-defined functions. Create a
script called `function_basics.py`:

```bash
code function_basics.py
```

## Calling a Function

Add the following lines to your script:

```python
import random

r = random.random()
five = int('5')
print(five, r)
```

The term for using a function in Python is to *call the function*
or *invoke the function*. To do so, we:

1. Write the function's name, such as `int` in the example above.
2. Include a *function argument list*, which is a balanced
set of parentheses `()`. Do not add a space between them
and the function's name, so `int()` is valid, but `int()` is not.
3. If the function requires it, provide an *argument* inside
the argument list. Here, `'5'` is the argument in `int('5')`
Notice that `random.random()` does not require arguments.
4. If the function accepts (or requires) more than one argument,
separate them by commas. Here `print(five, r)` has two arguments:
`five` and `r`.

Function arguments enable us to communicate information that
the function needs to perform its job, or to alter its default
behavior. We say that we *pass an argument* to a function,
such as passing `'5'` in the function call `int('5')`.

We'll sometimes speak of the *caller of the function* to
describe where the function call happened in the code.

## Function Return Values

In Python, every function is an expression, which means
that every function produces a value. This value is
known as the **function return value**.

- In the example above, the return value of `random.random()`
is a random `float` number, and we stored it in the
variable `r`.
- The return value of `int('5')` is the integer `5`, and we
stored it in the varible `five`.

If a function has a return value, it's not necessary to save
it in a variable. We can, for example, use it directly in
an expression, or not at all (though this may not be useful).

## Side Effects and the `None` Object

We said that every function in Python has a return value.
Indeed, even the `print()` function does. Add the following:

```python
my_none_variable = None
print(f"{my_none_variable=} has type {type(my_none_variable)}")

return_value_of_print = print("Hello")
print(f"The print() function returned: {return_value_of_print}")
```

In Python, `None` is a special object of type `NoneType`, and it
is the only object of that type. It represents the absence of
a value. As we will see later, functions use the `return` keyword
to provide the return value. A function may omit the keyword,
and in this case, its return value is `None`.

We will learn more about `None` later.

## Positional Arguments

In the examples above, we provided **positional arguments** to our
functions. Behind the scenes, as we will see, defining a function
requires specifying parameters, and the order in which these are
defined imposes the order in which we pass the arguments.
Using positional arguments entails passing the value and nothing
else. For example, in

```python
print(five, r)
```

`five` is the first positional argument, and `r` is the second
positional argument.

## Keyword Arguments

Python allows the use of **keyword arguments**. For this,
we must know the name of the function parameter because
we have to explicitly name it. An advantage of keyword arguments
is that we can pass the arguments in any order
