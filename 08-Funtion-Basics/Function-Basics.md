# Functions

In computer programming, a **function** is a unit of code that has
a name and performs one specific job.

Functions are useful because they group related logic together, providing
a layer of abstraction. You do not have to understand, for example, how a
microwave relies onelectromagnetic waves or other difficult physics concepts
to use it. You just have to know that if you press buttons to enter a duration
and press the "start" button, it will heat up your food.

There are many types of functions in Python:

- **Built-in functions**: These are provided by Python and have special
language support, but are otherwise functions like any other.
Examples include `print()`, `type()`, `input()`, and `len()`.

- **Library functions**: These are functions available through modules
such as the `math` module. Examples include `math.exp()` and `math.sin()`.

- **Methods**: These are also just functions, but they are called to
action on specific objects. For example, if `s` is a string object (type `str`),
then the `upper()` method, called as `s.upper()`, produces the uppercase
version of the string `s`.

- **User-defined functions**: Any user of Python can create functions
of their own! This is the focus of this section.

## Calling a Function

The act of using a function in Python is known as **calling a function** or
**invoking a function**. How you call a function is dependent on its interface.
In general, we call a function by:

- Writing its name, such as `myfunction`.
- Adding a balanced set of parentheses `()`, such as `myfunction()`.
- Providing arguments, if any, within the parentheses, separated by
commas if there's more than one.

### Function Arguments

A **function argument** is a value that we provide to a function so that
it can perform its job. When we provide an argument to a function, we often
say that we *pass an argument* to the function.

Create a script `functions_basics.py`:

```bash
code functions_basics.py
```

Add the following:

```python
import random

r = random.random()
five = int('5')
print(five, r)
```

In the example above:

- The `random.random()` library function does not require any arguments to
perform its singular job, which is to display a value.
- The `int()` built-in function takes a single argument of type string (`str`).
Here we pass the number literal `5` as an argument. It's designed
to produce an `int` from its argument.
- The `print()` function can accept multiple arguments, separated by commas.
Here, we pass the variables `five` and `r`, separated by a comma `,`. Its job
is to display each one, separated by a single space.

### Return Value of a Function and `None`

In computer programming, a function may **cause a side effect** or
**produce a return value**, or both. A **return value** is a value
that the function provides to its user once the function has finished.
In the same way that the user of a function communicates with it by
passing it an argument, the function communicates with its caller
by returning a value.

In the example above:

- `random.random()` returns a `float` value that we store in the `r` variable.
- `int('5')` returns an `int` value that we store in the `five` variable.

As it turns out, `print()` also returns a value, but we chose not to store it.
The return value of `print()` is the special value `None`, which is an object
that Python uses the signify the absence of a value. In fact, `None` is also
a literal.

Add the following to your script:

```python
my_none_variable = None
print(f"{my_none_variable=} has type {type(my_none_variable)}")
return_value_of_print = print("Hello")
print(f"The print() function returned: {return_value_of_print}")
```

Notice that `None` is not a string; it has its own type `NoneType`, and no
other variable is of this type. This `None` abstraction can be useful, as we will soon see.

Usually (but not always), functions that return `None` have a *side effect*.

The [Wikipedia entry on side effect](https://en.wikipedia.org/wiki/Side_effect_(computer_science))
says:

> a function is said to have a side effect if it has any observable effect other than its primary effect of reading the value of its arguments and returning a value to the invoker of the operation.

For example, the side effect of `print("Hello")` is to display `hello` on your
screen.

## Defining a Function

Add the following to your Python script:

```python
def greet_user():
    """Display a friendly greeting."""
    pass
```

This a function that (at this point) does nothing. Let's go
through its components:

1. To define a function in Python, we first use the `def` keyword.
2. We enter a blank (coventionally a single one).
3. We enter the name of the function, here `greet_user`. The name is subject to similar
rules and conventions as variables (snake case).
4. We include parentheses `()` which define the *parameter list*. Optionally,
we include variable names, separated by commas, for each parameter of the
function.
5. Optionally, you may include a *docstring*, short for *documentation string*.
This is a triple-quoted string containing a message explaining what the
function does. Here, the docstring is `"""Display a friendly greeting"""`.
We will discuss docstrings more later on, but for now, consider putting
a short description. Code editors like VS code will show you this description
when you hover over a function's name, and Python will also display it
if you use the `help()` built-in function.
6. We include the *function body*, which are the lines of code that
should run when this function is called. The lines of code in the
function's body must always be indented relative to the `def` keyword,
or Python will issue an error. It is recommended that you indent with
four spaces. Here, the body consists of the keyword `pass`, which is a
statement in Python that does nothing.

Let's update this function's body to have the following code:

```python
def greet_user():
    """Display a friendly greeting."""
    print("Hello, world!")
```

If you run your script, you will observe that nothing happens.
Alas, we've  *defined our function*, but we *did not call it*.
Update your code as follows:

```python
def greet_user():
    """Display a friendly greeting."""
    print("Hello, world!")

greet_user()
```

Observe that this line is *not* indented, reflecting that it is
not part of the function's body. Moreover, I use a space to
separate the function call from the function definition. You
should see:

```text
Hello, world!
```

## Function Parameters

Say that we want our `greet_user()` function to be personalized.
Update your code as follows:

```python
def greet_user(user):
    """Display a personalized greeting"""
    print(f"Hello, {user.title()}!")

greet_user("sergio")
greet_user("denzel")
greet_user("christine")
```

We included `user` inside the parentheses in the function header,
known as the *parameter list*. This makes `user` a **function parameter**.
