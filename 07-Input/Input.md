# Input

We've seen how to display output to the screen with the `print()`
built-in function. The corresponding function for obtaining input
is the `input()` built-in function.

The `input()` function works as follows:

- We call it by giving it a string as an argument. The string
is a message that is displayed to the user. The purpose of the
message is to explain what they should enter, and this is sometimes
known as a *prompt*.
- Our program then pauses to allow the user to enter a message.
- The program continues when the user presses the
`ENTER` (or `RETURN`) key on their keyboard, signifying that they
are done providing input.
- The `input()` function produces the text that the user typed
as its (string) value.

Create a Python script called `getting_input.py`:

```bash
code getting_input.py
```

Enter the following:

```python
value_entered_by_user = input("Please enter a number: ")
print(f"You entered {value_entered_by_user}, and it has type {type(value_entered_by_user)}")

more_user_input = input("Enter anything else: ")
print(f"You entered {more_user_input}, and it has type {type(more_user_input)}")
```

If you run this program, you will see that the `print()` statement does not
run immediately because the program pauses until the user provides input.
Notice also that the type of both values is `str`, even if you enter a number.
This is important because it means we cannot perform mathematical operations
with the input.

## Converting Numeric `str` Objects to `int` or `float`

Well, what if we did want to interpret a number entered by the user as a number?
To do so, we can use the `int()` and `float()` built-ins. For example:

```python
four_as_a_string = '-4'
four = int(four_as_a_string)
print(f"The type of {four_as_a_string=} is {type(four_as_a_string)}")
print(f"The type of {four=} is {type(four)}")

pi_as_a_string = '3.14'
my_pi = float(pi_as_a_string)
print(f"The type of {pi_as_a_string=} is {type(pi_as_a_string)}")
print(f"The type of {my_pi=} is {type(my_pi)}")
```

The `int()` built-in function accepts (among other things) a `str` object
(a string) as an argument, and produces an integer (an `int`). Similarly,
`float()` may convert a `str` to a `float`. Notice that if the argument
we provide is not a string, the program will terminate with an error
(known as an exception in Python). We will learn how to handle this
in the future.

With this, we can write a useful interactive program. For example,
we can use the `math.gcd()` function to compute the greatest common
divisor of two positive integers provided by the user. Create a Python
script called `mygcd.py`:

```bash
code mygcd.py
```

Enter the following:

```python
import math

print("Welcome to my greatest common divisor program")

m_input = input("Enter a positive integer: ")
n_input = input("Enter another positive integer: ")

m = int(m_input)
n = int(n_input)

print(f"The greast common divisor of {m=} and {n=} is {math.gcd(m, n)}")
```

Notice that the user may not enter a number, causing your program to
have an error because `int()` will fail to convert it to a number.
This might be by mistake or on purpose. For example, the user might
enter `4.0`, which our program cannot handle with `int()` (it would
need `float()`).

In general, you should never trust your user's input, and you should
code defensively. We will learn ways to do this as we move along.
