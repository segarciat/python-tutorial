# Variables

A **variable** is a label (name) used to refer to a value. In Python,
a valid variable adheres to the following rules:

- It may consist of letters (uppercase or lowercase), numbers, and underscores.
- It may not start with a number.

The following are strongly recommended guidelines for variables:

- Use lowercase letters only (numbers are alright when appropriate).
- If the variable name has multiple words, use an underscore `_` to
separate each word (since spaces are not allowed).
- Use all uppercase letters for constants (discussed later).
- Do not use a variable with the same name as a built-in function,
a Python keyword, or any other function. For example, `for` is a Python
keyword, so it cannot be used as a variable name.

This convention is often known as *snake case*. Another convention
used in other programming languages is called *camel case*.

Begin by creating a script called `variables.py`:

```bash
code variables.py
```

## Defining a Variable

To define a variable, we pick a name of our choise, and then use the
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

As you can see, this code creates two variables named `width` and `height`.
The vaue of `width` is `8`, and the value of `height` is `15`. Notice the
use of a single space on both sides of the equal sign when defining a variable.
This is recommended convention to make code more readable.

As you can see, we can refer to the variables in other places to access their
value and to perform computations. For example, we defined an `area` variable
whose value is the result of multiplying the value of `width` and `height`.
Similarly, we used the value of `width` and `height` to define a variable called
`perimeter`.

If you run the script, you should see:

```text
120
46
```

In Python, we can reassign a variable so that it can be a different value.
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

Notice that although width and height change, the value of the variables
`area` and `perimeter` remains the same as when we computed them with
the old values of `width` and `height`. If we wish them to account for
the new area values, we would need to reassign `area` and `perimeter`
via the same computation. This could become repetitive, but it is necessary
for correctness, if that's what we intend. Later we will learn of ways
to reduce code repetition.

We can use variables with other data types, not just numbers, as we will see.

## Constants and "Magic Numbers"

A **constant** is a variable whose value stays the same throughout the
duration of the program. The convention in Python is to use upper snake
case for variable, meaning all uppercase letters, with compound words
using an underscore to separate words.

```bash
E = 2.71828
GOLDEN_RATIO = 1.618
GRAVITY_ACCELERATION = 9.81
```

Keep in mind that the notion of constant variable is a convention, and
it is not enforced by the language. For example, you can certainly
reassign the value of a (constant) variable without any errors.
However, this is frowned upon, and you are advised to not change the
value of a constant once it is defined.

Constant variables help with limiting the use of **magic numbers**,
which are literal values that have unexplained meaning or for which there are
multiple occurrences. For example, suppose we are doing physics calculations,
and we find ourselves using the value `9.81` often, the free-fall acceleration
due to gravity in the units of meters per seconds squared. Including this number
everywhere is an option, but it is not advised because its meaning may not be clear.
In this example, `9.81` is a magic number, and it is preferred to use a constant
variable whose value is  `9.81`.

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
