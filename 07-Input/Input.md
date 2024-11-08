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
as its (string) value. The result is always of type `str`.

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
`float()` may convert a `str` to a `float`. Notice that if the string
we provide is not a number, the program will terminate with an error
(known as an exception in Python). We will learn how to handle this
in the future.

With this, we can write a useful interactive program. For example,
the equation $I = Prt$ is called the **simple interest** formula.
Given a principle amount $P$, an interest rate $r$ as a number
between 0 and 1, and a value $t$ for the number of time periods,
we can calculate $I$, the interest accrued during that period.
We will write a program that computes this quantity for a user.

Create a Python script called `simple_interest.py`:

```bash
code simple_interest.py
```

First, we will welcome the user, and explain what the program
will entail:

```python
print("""
    Welcome to my Simple Interest program!

Please follow the instructions and I will do the interest
computation for you.
""")
```

Next, we will need to prompt the user for inputs:

```python
principal_input = input("Enter the principal to the nearest dollar: ")
interest_rate_input = input("Enter the yearly interest rate as a percent (1 to 100): ")
number_of_periods_input = input("Enter the number of periods in years: ")
```

Since `input()` produces a string, which has type `str`, it follows that
all three variables above are of type `str`. We need to convert them
to number types so that we can perform arithmetic:

```python
# Convert data from str to appropriate number type
principal = float(principal_input)
yearly_rate = float(interest_rate_input)
years = float(number_of_periods_input)
```

We need to do this so that we can multiply the quantities.
Next, we will do the calculation, and display the result:

```python
# Compute and display the result
interest = round(principal) * (yearly_rate / 100) * years
print(f"According to our simple interest rate formula, the interest amout is ${interest:.2f}")
```

The computation itself is very simple. Note that we use the
`round()` function, in case the user did not enter an amount
to the nearest dollar as we asked. Also, though we expect a user
to provide a percentage, our formula actually uses its equivalent
version as a number between 0 and 1, so we divided the interest
rate by 100.

We used a format string to display a complete sentence so the user
has some context on what we did. Notice the funny notation `{interest:.2f}`.
This is special formatting supported by f-strings:

1. We write a colon `:` in the braces `{}` of an f-string.
2. To the left of the colon, we have the expression we want to display
(in this case, the value of the `interest` variable).
3. To the right of the colon, we have `.2f`, which means
"display this float with 2 digits after the decimal".

See [more format examples](https://docs.python.org/3/library/string.html#format-examples)
in the Python documentation. I've only mentioned it to pique your
curiosity, but there's no need to worry about it much otherwise for now.

Below is a sample run of the program:

```

    Welcome to my Simple Interest program!

Please follow the instructions and I will do the interest
computation for you.

Enter the principal to the nearest dollar: 10000
Enter the yearly interest rate as a percent (1 to 100): 0.5
Enter the number of periods in years: 3
According to our simple interest rate formula, the interest amout is $150.00
```

## Caution with User Input

Notice that the user may not enter a number, causing your program to
have an error because `float()` will fail to convert it to a number.
This might be by mistake or on purpose. For example, the user might
enter `five` instead of `5`, which would not work because `input()`
would produce the string `"five"`, which cannot be converted to
a `float` by `float()`. The conversion is necessary because we
we cannot multiply strings together; we multiply numbers!

Notice also that we used one variable for the input from the user
and one for the result after conversion. To be concrete, `number_of_periods_input`
is a `str`, the result of `input()`, which contains what the user
typed. Meanwhile, `years` is a `float`. We say that we *convert*
the from a `str` to a `float` in this case. Keep in mind, though,
that the `number_of_periods_input` variable is still a label for
a `str` object, so the underlying object it is a label for does
not change, nor does `number_of_periods_input` suddenly become
a label for a different object. Rather, the desired value of the
desired type is produced, and we saved a reference to it in
the `years` variable.

There are ways to re-write the program to eliminate the intermediate
variable, such as by *nesting* the `int()` and `input()` function calls
as follows:

```python
years = float(input("Enter the number of periods in years: "))
```

In this case, the output of `input()`, which is a string, is immediately
passed as an input argument to `int()`. Therefore, if the user entered
a valid number, there will not be an error, and `years` will be a `float`
representing the number the user entered. This option might seem
appealing, but you are cautioned against it. For example, this precludes
verifying that the user entered something valid. This is why we
have chosen to apply some of the computations, such as rounding or
dividing by 100, after-the-fact.

In general, you should never trust your user's input, because your user
may make a mistake, or they may maliciously enter an invalid value.
For example, your user may enter `3.0` thinking that is valid, which
would fail for `int()` (though not for `float()`). Though it's impossible
to anticipate everything the user will do, we will learn ways to
make our programs robust, to limit the ways that it terminates in errors
that the user cannot understand.