# Variables

A **variable** is a label (name) used to refer to a value. In Python,
a valid variable adheres to the following rules:

- It may consist of letters (uppercase or lowercase), numbers, and underscores.
- It cannot not start with a number.

The following are strongly recommended guidelines for variables names:

- Use lowercase letters only (numbers are alright when appropriate).
- If the variable name has multiple words, use an underscore `_` to
separate each word (since spaces are not allowed). This is known as
*snake case*.
- Use all uppercase letters for constants (discussed later).
- Do not use a variable with the same name as a built-in function,
a Python keyword, or any other function. For example, `for` is a Python
keyword, so it cannot be used as a variable name. Similarly, do not
use a variable name `print`, since it may the `print()`
function.

Begin by creating a script called `variables.py`:

```bash
code variables.py
```

## Defining a Variable

To define a variable, we pick a valid name, and then use the
*assignment operator*, the `=` symbol, followed by a value we wish
for our variable to represent.

Type the following:

```python
width = 8
height = 15

area = width * height
perimeter = (width * 2) + (height * 2)

print(area)
print(perimeter)
```

As you can see, this code defines two variables named `width` and `height`.
When Python encounters the name `width` in an expression, it will replace
it with the value `8`; similarly, when it encounters `height`, it will replace
it with the value `15`. Notice the use of a single space on both sides of the
equal sign when defining a variable. This is recommended convention to make code
more readable.

As you can see, we can refer to the variables in other places to access their
value and to perform computations. For example, we defined an `area` variable
whose value is the result of multiplying the value of `width` and `height`.
Similarly, we used the value of `width` and `height` to define a variable called
`perimeter`. Also, we provided `area` and `perimeter` as arguments
when calling the `print()` function.

If you run the script, you should see:

```text
120
46
```

In Python, we can reassign a variable so that it can take on a different value.
Add the following lines of code:

```python
width = 0.7
height = 1.2

print(width)
print(height)

print(area)
print(perimeter)
```

You will see:

```text
0.7
1.2
120
46
```

Notice that although `width` and `height` change, the value of the variables
`area` and `perimeter` remains the same as when we computed them with
the old values of `width` and `height`. It's possible you may want
`area` and `perimeter` to reflect the updated values of `width` and `height`.
Alas, to do that, we would need to add code performing the same computation,
like so:

```python
width = 0.7
height = 1.2

print(width)
print(height)

print(area)
print(perimeter)

area = width * height
perimeter = (width * 2) + (height * 2)

print(area)
print(perimeter)
```

This repetition is not great, but  later we will learn ways to mitigate this.

## Constants and "Magic Numbers"

A **constant** is a variable whose value stays the same throughout the
duration of the program. The convention in Python is to use upper snake
case for variable, meaning all uppercase letters, with an underscore between
each word (since spaces are not allowed):

```python
E = 2.71828
GOLDEN_RATIO = 1.618
GRAVITY_ACCELERATION = 9.81
```

Keep in mind that the notion of constant variable is a convention, and
it is not enforced by the language. For example, you can certainly
reassign the value of a (constant) variable without any errors,
just like we did for `width`, `height`, `area`, and `perimeter`.
However, this is frowned upon for constants, and you are advised to not
change the value of a constant once it is defined.

Constant variables help with limiting the use of **magic numbers**,
which are literal values in our scripts that have unexplained meaning or for
which there are multiple occurrences. For example, suppose we are doing
physics calculations, and we find ourselves using the value `9.81` often, the
free-fall acceleration due to gravity in the units of meters per seconds squared.
Including this number everywhere is an option, but it is not advised because its
meaning may not be clear. In this example, `9.81` is a magic number, and it is
preferred to use a constant variable whose value is  `9.81`.

The `math` module has some constants which do not adhere to the uppercase
convention, but this is intentional and are an exception, not a rule.
For example, `math.e` is Euler's number, `math.pi` is $\pi$.

Here's a summary of constants:

- A constant variable is a convention for a variable whose value should not change.
- Constants use the upper snakecase convention makes constants stand out.
- Constants adds clarity about our intention in the source code.
- If we decide to change the value of the constant, we can do it in one place.
For example, we may wish to express gravity in units of feet per second squared,
in which case its value is 32, or we may want to make it just `9.8` instead of `9.81`.
