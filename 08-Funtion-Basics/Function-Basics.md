# Functions

In computer programming, a **function** is a unit of code that has
a name and performs one specific job.

Functions are useful because they group related logic together, providing
a layer of abstraction. You do not have to understand, for example, how a
microwave relies onelectromagnetic waves or other difficult physics concepts
to use it. You just have to know that if you press buttons to enter a duration
and press the "start" button, it will heat up your food.
Similarly, you do not have to understand how the `print()` function works
internally to use it.

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

- **User-defined functions**: Any Python programmer can create functions
of their own! This is the focus of this section.

## Calling a Function

The act of using a function in Python is known as **calling a function** or
**invoking a function**. How you call a function is dependent on its interface.
In general, we call a function by:

- Writing its name, such as `myfunction`.
- Adding a balanced pair of parentheses `()`, such as `myfunction()`.
- Providing arguments, if any, within the parentheses, separated by
commas if there's more than one.

### Function Arguments

A **function argument** is a value that we provide to a function so that
it can perform its job. When we provide an argument to a function, we often
say that we *pass an argument* to the function.

Create a script `existing_functions.py`:

```bash
code existing_functions.py
```

Add the following:

```python
import random

r = random.random()
five = int('5')
print(five, r)
```

If you run it, you may see output similar to:

```text
5 0.43342671879642525
```

In the example above:

- The `random.random()` library function does not require any arguments to
perform its singular job, which is to generate a random fractional number
between 0 and 1.
- The `int()` built-in function takes a single argument of type string (`str`).
Here we pass the string literal `'5'` as an argument. It's designed
to produce an `int` from its argument, in this case the `int` value `5`.
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
Python in general is case sensitive, so you need to match the casing of `None` exactly.

Usually (but not always), functions that return `None` have a *side effect*.

The [Wikipedia entry on side effect](https://en.wikipedia.org/wiki/Side_effect_(computer_science))
says:

> a function is said to have a side effect if it has any observable effect other than its primary effect of reading the value of its arguments and returning a value to the invoker of the operation.

For example, the side effect of `print("Hello")` is to display `hello` on your
screen.

## Defining a Function

Add the following to your Python script:

```python
def do_nothing():
    """This function does nothing."""
    pass
```

This a function that (at this point) does nothing, as you may guess
from the string description. Let's go through its components:

1. To define a function in Python, we first use the `def` keyword.
2. We enter a blank (coventionally a single blank).
3. We enter the name of the function, here `greet_user`.
The name is subject to similar rules and conventions as variables (snake case).
4. We include parentheses `()` which define the *parameter list*. Optionally,
we include variable names, separated by commas, for each parameter of the
function.
5. Optionally, you may include a *docstring*, short for *documentation string*.
This is a triple-quoted string containing a message explaining what the
function does. Here, the docstring is `"""This function does nothing."""`.
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

We will add a more useful function. Update your Python script to
look as follows

```python
def welcome_user():
    """Displays friendly messages when the program starts."""
    print("Welcome to my program!")
    print("I hope you are having a good day.")
```

Notice this is similar to `do_nothing()`, but `pass` has been
replaced by two functions call to `print()`. Functions may call
other functions, as you can see. However, if you run your script,
you will observe that nothing happens. Alas, we've  *defined our function*,
but we *did not call it*.

Update your code as follows:

```python
# Define a function that does nothing.
def do_nothing():
    """This function does nothing."""


# Define a function with no inputs, nor return values, but produces text.
def welcome_user():
    """Displays friendly messages when the program starts."""
    print("Welcome to my program!")
    print("I hope you are having a good day.")

# Call the functions we defined.
do_nothing()
welcome_user()
```

Observe that the function calls following the definitions are *not*
indented, reflecting that they are not part of the function's body.
Moreover, I use a space to separate the function call from the
function definition for readability.

When you run this script, you will see:

```text
Welcome to my program!
I hope you are having a good day.
```

### Function Parameters

What if we wish to personalize the welcome message? For this,
we can use a function parameter.

Create a script called `function_parameters.py`, and add the following:

```python
def greet(username):
    """
    Displays a personalized greeting.
    
    :param str username: A name as a string.
    """
    print(f"Welcome back, {username}!")

user_input = input("Please enter your name: ")
greet(user_input)
```

Here's a sample interaction after running the program:

```
Please enter your name: sergio
Welcome back, sergio!
```

Here, the `username` function in the definition of `greet()`
is a **function parameter**. This is a variable that our
function needs in order to accomplish its job. This should
remind you of a *function argument*.

- A function parameter appears in a *function definition*.
It is a variable name listed inside the function parameter
list. The only parameter to the `greet()` function is `username`.
This variable is only valid inside the function body.

- A function argument appears in a *function call*. It
could be a variable, but it does not have to be; it can
be any Python expression. In the call `greet(user_input)`,
the `user_input` variable is an argument (which is a string).

### Multiple Function Parameters

We can require more than one parameter by separating the
names with commas in the function parameter list:

```python
import random

def generate_lucky_number(smallest, largest):
    """
    Displays a random number in the range defined by the user.

    :param str smallest: The smallest number in the range (included).
    :param str highest:  The largest number in the range (included).
    """
    lucky_number = random.randint(smallest, largest)
    print(f"Drum roll... your lucky number is: {lucky_number}.")
```

We will use this function to write a simple program that generates
three numbers for the user. Update your script as follows:

```python
import random

def generate_lucky_number(smallest, largest):
    """
    Displays a random number in the range defined by the user.

    :param str smallest: The smallest number in the range (included).
    :param str highest:  The largest number in the range (included).
    """
    lucky_number = random.randint(smallest, largest)
    print(f"Drum roll... your lucky number is: {lucky_number}.")


small_number_input = input("Enter an integer: ")
large_number_input = input("Enter a bigger integer: ")

minimum = int(small_number_input)
maximum = int(large_number_input)

# Generate lucky numbers.
print(f"Generating lucky numbers between {minimum} and {maximum}...")

generate_lucky_number(minimum, maximum)
generate_lucky_number(minimum, maximum)
generate_lucky_number(minimum, maximum)
```

Here's a sample interaction when running this program:

```text
Enter an integer: 3
Enter a bigger integer: 100 
Generating lucky numbers between 3 and 100...
Drum roll... your lucky number is: 19.
Drum roll... your lucky number is: 72.
Drum roll... your lucky number is: 80.
```

Notice how we can call our function multiple times,thus reusing our
logic. This is a good step towardsreducing code duplication.
Soon we will learn about loops, which help further with this.

### Positional Arguments and Keyword Arguments

You may have noticed that the order in which we pass arguments
to a function matters. Create a script called
`positional_and_keyword_arguments.py`, and add the following codE:

```python
introduction = "Hi, I am Peggy."
more_details =  "I am a 9 year-old cat."
closing = "I am going to nap. Bye!"
print(introduction, more_details, closing)
```

If you run this script, you will see:

```text
Hi, I am Peggy. I am a 9 year-old cat. I am going to nap. Bye!
```

Here, `introduction` is the first argument, `more_details` is the
second, and `closing` is the third. This is an example of calling
a function with **positional arguments**. This means that the
order matters, and if you re-order the variables, the output
will be different. For some functions, re-ordering the variables
may cause an error, because the function expects the arguments
in a specific order.

An alternative is calling a function with **keyword arguments**.
Add the following to your script:

```python
approximately_pi = round(3.14159, ndigits=2)
print(approximately_pi)
```

Here, `ndigits` is a keyword argument of the `round()` built-in function.
To provide keyword arguments, we need to know the name of the
parameters of the function ahead of time. The syntax for
passing keyword arguments is as follows:

- We write the name of the function parameter. In this case,
it is `ndigits`.
- We write an `=` sign. Conventionally, we do not include
a space between the parameter name and the `=`.
- We provide the value for the parameter. Above, we provided
`2`. Conventionally, do not put a space between the `=` and the
value.

Notice that this does not define a variable named `ndigits`
accessible to us. Rather, it sets the `ndigits` parameter of
the `round()` function.

Keyword arguments are useful when we do not remember the order
in which we should pass arguments to a function because
they allow us to pass the parameters in any order:

For example, recall we defined a `generate_lucky_number()`
function in `multiple_parameters.py` with a `smallest`
and `largest` argument. We could call the function with
keyword arguments as follows:

```python
generate_lucky_number(smallest=minimum, largest=maximum)
generate_lucky_number(largest=maximum, smallest=minimum)
generate_lucky_number(minimum, largest=maximum)
```

Notice in the first two calls, the change the order of the
keyword arguments.

Note also that in the last call, we pass `minimum` as a positional
argument and `maximum` as a keyword argument. This is valid, too.
However, one restriction is that once we pass a keyword argument,
all arguments that follow it must be passed as keyword
arguments not positional. Therefore, the following would
result in an error:

```python
# cannot have positional parameters after keyword arguments
generate_lucky_number(largest=maximum, minimum)
```

### Return Values

The last thing we will discuss is **return values**.
Create a script `return_values.py`, and add the following code:

```python
def average(x, y):
    """
    Computes the average of two numbers.

    :param float x: Any number.
    :param float y: Any number.
    :return: The average of the inputs.
    """
    return (x + y) / 2

x_input = input("Enter a number: ")
y_input = input("Enter another number: ")

x = float(x_input)
y = float(y_input)

average_of_xy = average(x, y)

print(f"The average of {x} and {y} is {average_of_xy}.")
```

Here's a sample interaction with this program:

```text
Enter a number: 3
Enter another number: 7
The average of 3.0 and 7.0 is 5.0.
```

Notice that the function uses the `return` keyword followed
by the expression `(x + y) / 2`. The result will be available
to whoever called `average()`. For example, they can choose
to store it in a variable, like we did, or use it in another
expression directly.