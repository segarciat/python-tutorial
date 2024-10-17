# If Statements

Now that we have discussed Booleans, let's return to the "guess my number"
game we alluded to earlier. Create a script `guess_my_number_1_attempt.py`:

```bash
code guess_my_number_1_attempt.py
```

Add the following code:

```python
import random

MINIMUM = 1
MAXIMUM = 100

secret_number = random.randint(MINIMUM, MAXIMUM)

print(f"I'm thinking of a number between {MINIMUM} and {MAXIMUM}... guess!")
user_guess = input("Your guess: ")

if not user_guess.strip().isdigit():
    print("Your guess should only contain digits...")
elif int(user_guess) == secret_number:
    print("That's correct!")
else:
    print(f"That's too bad. The number was {secret_number}!")
```

Let's run through the program:

1. We import the `random` module, and use the `random.randint()` function
to generate a random integer between 1 and 10.
2. We provide the user with instructions with `print()` and prompt thme to
guess using `input()`
3. We use an `if` statement to determine whether the user provided
valid input. The expression `not user_guess.strip().isdigit()` is
`True` when the user provides an input that has at least one non-digit character.
If that is the case, we inform the user and do nothing else. That is,
the code under `elif` and under `else` do not execute. Otherwise,
the code in the `if` block does not execute and we move on.
4. If condition tested in the `if` is `False`, the condition in the `elif`
is evaluated. In this case, we convert the user's guess to an integer with
`int(user_guess)` and compare it against `secret_number`. If the numbers
are equal, we congratulate the user. Otherwise the code in the `elif` block
does not execute.
5. If the user's input was a number but not the correct one, the code
under `else` executes.

## What's an `if` statement?

In Python, an `if` statement is a tool used for control flow.
The general format is as follows:

```text
# some code before if
if <condition>:
    <body: runs when condition is true>

# Some code after if, which runs whether or not the condition was true
```

There are a few parts here:

1. The `if` keyword made available by Python.
2. An expression that is converted to a Boolean, known as the
*controlling expression*.
3. A colon `:` after the controlling expression, just like in
function definitions.
4. The *body* of the `if` statement, indented at a 4 space offset
of the `if` keyword; this is similar to functions. This consists
of one or more Python statements (lines) that will execute only
if controlling expression evaluates to `True`.

Create a file `if_basics.py`:

```bash
code if_basics.py
```

Define the following function:

```python
m = 7
divisor = 3
description = "is an integer"

if m % divisor == 0:
    description += f", and it is divisible by {divisor}"
    description += f", fits {m // divisor} times into {divisor}"

print(f"{m=} {description}")
```

If you run it, you will see:

```text
m=7 is an integer
```

The controlling expression `m % divisor == 0` evaluates to `False` because
the remainder of dividing `7` by `3` is `1`, not `0` (put another way,
`7` is not divisible by `3`). Therefore, the statements in the body of
the `if` statement did not execute. Notice the code after the `if`
(the unindented `print()`) still executes, since it is not part of
the `if` body.

If we do the same below, now with a variable `n` set to `114`, by adding the
following (repeated) code underneath:

```python
n = 114
divisor = 3
description = "is an integer"

if n % divisor == 0:
    description += f", and it is divisible by {divisor}"
    description += f", fits {n // divisor} times into {divisor}"

print(f"{n=} {description}")
```

Then we see the output:

```text
m=7 is an integer
n=114 is an integer, and it is divisible by 3, fits 38 times into 3
```

This time, the statements in the body of `if` executed, because `114 % 3 == 0`
evaluates to `True`. Notice the code after the `if` (unindented) still
executes. On an slightly unrelated note, we could have reduced this
code repetition by defining a function if we wished.

## The `else` branch

Sometimes we want to execute something only when the controlling
expression of the `if` is `False`. For example, an integer may
only be even or odd. Add the following:

```python
if m % 2 == 0:
    print(f"{m} is even")
else:
    print(f"{m} is odd")
```

Here's another example. Create a file `flip_coin.py`:

```bash
code flip_coin.py
```

Add the following:

```python
import random

def flip_coin():
    """Simulates flipping a coin. Returns "Head" or "Tails" with equal probability.

    Returns:
        str: "Heads" or "Tails"
    """
    if random.random() < 0.5:
        return "Heads"
    else:
        return "Tails"


# Flip coin a few times
print(flip_coin())
print(flip_coin())
print(flip_coin())
```

If you run this, you might see:

```text
Heads
Heads
Tails
```

However your results may vary. Recall the `random()` method in the `random`
module, or `random.random()`, generates a floating point number from a uniform
distribution on the interval from 0 to 1. We've instrumented this library to
create `flip_coin()`, a function that does not take any inputs, and it produces
the string `"Heads"` or `"Tails"` depending on whether the number generated is
between `0`and `0.5` or between `0.5` and `1`.

## The `elif` branch

Sometimes we want to a code block to execute when the controlling
expression for `if` is `False`, but we don't want that new code
block to execute unconditionally as is done with `else`. In effect,
we want a new controlling expression that only evaluates when
the `if` controlling expression is `False`. That is the purpose of
`if`. We've seen this in our original example:

```python
if not user_guess.strip().isdigit():
    print("Your guess should only contain digits...")
elif int(user_guess) == secret_number:
    print("That's correct!")
else:
    print(f"That's too bad. The number was {secret_number}!")
```

When `not user_guess.strip().isdigit()` is `False`,
we know that `user_guess.strip().isdigit()` is `True`, because
`not` flips the Boolean ("truth") value. Hence, the user entered
a valid number. Only in this case do we want to attempt to convert
their input string to an integer with `int()`. Why go through this?
Recall that if `int()` receives a string that is not a valid integer,
it results in an Exception, such as this interaction in the REPL:

```text
>>> int("3.14")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.14'
```

We don't want this error to occur because it would break our program,
and our user might panic upon seeing this. The controlling expression
`not user_guess.strip().isdigit()` is effectively *guarding* against
an error.

## Resources

- Check out some more examples at [W3schools](https://www.w3schools.com/python/python_conditions.asp).