# Booleans

Suppose we wish to create a number guessing game. Perhaps
we use the `random` module to generate a random integer
between 1 and 100, and then we ask the user to guess it.
How do we verify whether the user's input is correct?
To do this in Python, we might use an `if` statement,
which expects a *Boolean* expression, meaning an expression
that evaluates to `True` or `False`.

Create a file called `booleans.py`:

```python
code booleans.py
```

A **Boolean** is a data type representing only one of two
values. Python provides the literals `True` and `False`,
which are of type `bool` to represents Booleans:

```python
print(True)
print(False)
print(type(True))
print(type(False))
```

Note these are not string literals (there are no quotes anywhere).

## Producing Booleans With Relational Comparisons: `>`, `<`, `==`, and more

Python provides many operators many operators that can produce Boolean
results. The following operators work with numbers and strings:

- `x > y`: Produces `True` if `x` is greater than `y`, and `False` otherwise.
- `x >= y`: Produce `True` if `x` is greater than `y` or equal to `y`, and `False`
otherwise.
- `x < y`: Produces `True` if `x` is less than `y`, and `False` otherwise.
- `x <= y`: Produces `True` if `x` is less than or equal to `y`, and `False` otherwise.

For example:

```python
# True
print(1 < 7)
# False
print(-5 > 0)

# True
print(2 >= 2)

# True: apple sorts before orange alphabetically
print("apple" < "orange")

# False: lowercase a comes after uppercase O
print("apple" < "Orange")
```

A neat feature of Python (not commonly seen in other languages) is
that it lets you check that a quantity is in a range:

```python
x = 7

# True: x is 7, and it is between 1 and 10
print(1 < x < 10)

# False: x is not greater than 7
print(7 < x <= 10)
```

Python also provides the following for *all* data types (not just numbers and strings):

- `x == y`: Produces `True` if `x` and `y` are equal, and `False` otherwise.
- `x != y`: Produces `True` if `x` and `y` are different, and `False` otherwise.

Add the following to your script:

```python
# True
print(1 == (6 - 5))
# True
print(0 != (-3 - 3))
# False: first letters have different case
print("apple" == "Apple")
```

Notice that `==` has *two* equal signs, not to be confused with the assignment
operator which has one equal sign as in `x = 5`.


## Logical Operators: `not`, `and`, `or`

If you took a class in High School Geometry, you may have learned about *logic*,
where you learned about statements, which are sentences that have a True or False
value. You may also have learned of ways to combine them.

Booleans can also be combined with other booleans using **logical operators**.
These are:

- `not x`: Negates the value of `x`. If `x` is `True`, then `not x` is `False`,
and viceversa.

- `x and y`: The result is `True` if both `x` and `y` are `True`, and it is `False` otherwise.
In logic, a statement consisting of `and` is known as a *conjunction*.

- `x or y`: The result is `False` if both `x` and `y` are `False`, and it is `True` otherwise.
In logic, a statement consisting of `or` is known as a *disjunction*.

Continuing with the reference to logic from High School Geometry, you may also have learned
about *truth tables*. The following are truth tables for the `not`, `and`, and `not` operations:

|`x` | `not x`|
|----|--------|
| `True` | `False` |
| `False` | `True` |

|`x`| `y`| `x and y`|
|----|----|---------|
|`False`|`False`| `False`|
|`False`| `True`| `False`|
|`True` | `False`| `False`|
|`True`| `True`| `True`|

|`x`| `y`| `x or y`|
|----|----|---------|
|`False`|`False`| `False`|
|`False`| `True`| `True`|
|`True` | `False`| `True`|
|`True`| `True`| `True`|

Add the following to your code:

```python
# True: the result for or is True when at least one Boolean subexpression is True
print(5 < 0 or 5 > 0)

# False: Both expression must be True for their conjunction to be True
print(5 < 0 and 5 > 0)

# False: The remainder of dividing 5 by 2 is 1, not 0.
print((5 % 2) == 0)
```

The last expression is a common way to determine whether a number is even.
That is, the number is even if the remainder is zero. We can write a function
to encapsulate this:

```python
def is_even(n):
    """Determines whether the input integer is even.

    Args:
        n int: An integer

    Returns:
        bool: True if n is even, and False otherwise.
    """
    return (n % 2) == 0

# False
print(is_even(5))
```

The precedence of the logical operators is:

- `not` is highest precedence
- `and` is next highest
- `or` is lowest

When in dobut, use parentheses.

## DeMorgan's Laws

Sometimes it's useful to know transform a Boolean expression into
another equivalent expression. One reason we might do this is
before it's easier to understand.

We can use DeMorgan's Law, which consists of the following statements:

- `not (x and y)` is equivalent to `(not x) or (not y)`.
- `not (x or y)` is equivalent to `(not x) and (not y)`

In a way, it's as if we are distributing the `not`, but the `and`
changes to a `or`, and viceversa.

## The `in` Operator

Another operator that produces booleans is `in`. This operators
allows us to determine if a value belongs to a given collection.
Collection data types may store more than one value, and examples
include `list`, `set`, `tuple`, and `dict`. We will discuss
them in due time, but here's a brief example:

```python
list_of_numbers = [3, 5, 7]
set_of_strings = {"apple", "orange", "strawberry"}
tuple_of_coordinates = (1.5, -3.8)
dictionary_with_contacts = { "sergio": "sergio@email.com", "peggy": "peggy@email.com" }

# True: The value 7 is in the list
print(7 in list_of_numbers)

# False: "kiwi" is not in the set
print("kiwi" in set_of_strings)

# True: 0 is not in the tuple
print(0 not in tuple_of_coordinates)

# True: "sergio" is a key in the dictionary
print("sergio" in dictionary_with_contacts)
```

## Methods that Produce Booleans

Recall that objects in Python may have *methods*, which are functions
we can call directly on an object. Implicitly, the methods take the
object that we call the method on as an input. For example, strings
have an `upper()` method that produce a new string object, from the
given one, whose letters are all uppercase.

A Boolean method is one that produces a Boolean result. A common
convention is for Boolean method name to begin with the letters
*is*. To see this, start up the Python interpreter interactively:

```text
sgarciat@fx505gt:~/repos/Python-Tutorial$ python3
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Recall that a string object has class `str`. We can directly query
the class to check out what methods are available. Type `str.is`
and press the `TAB` key twice. This is a way to ask the interpreter
to either autocomplete for us, or to give us suggestions if more
than one alternative is possible. I see the following when I do this:

```text
sgarciat@fx505gt:~/repos/Python-Tutorial$ python3
Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> str.is
str.isalnum(  str.isascii(       str.isdigit(       str.islower(       str.isprintable(  str.istitle(
str.isalpha(  str.isdecimal(     str.isidentifier(  str.isnumeric(     str.isspace(      str.isupper(
>>> str.is
```

As you can see, there's a lot of options for method names, all beginning with
the word `is`. We can get help on any one of them. For example, we can
type `help(str.isdigit)` to learn about the `isdigit()` string method:

```text
>>> help(str.isdigit)
```

In my screen I see

```text
Help on method_descriptor:

isdigit(self, /) unbound builtins.str method
    Return True if the string is a digit string, False otherwise.

    A string is a digit string if all characters in the string are digits and there
    is at least one character in the string.
(END)
```

As you can see, the method returns `True` or `False`. The docstring also explains
what is considered a digit string. While you can do a web search whenever
you are not sure about what something does, using the built-in `help()` command
can be a great way to self-serve.

Add the following to your script

```python
# False: spaces don't count as digits
print("   12345 ".isdigit())
# True: strip() removes the leading and trailing spaces
print("   12345 ".strip().isdigit())
# False: The fractional dot . is not a digit
print("3.14".isdigit())
```

Check out how we chained two method calls

## Non-Booleans in a Boolean Context

Later on, we will encounter situations where we are using an expression that
is not a Boolean in a "Boolean context". For example, we may use a number
or a string as the condition expression for an `if` statement.

One way to see the truth value of each of the following is to pass the
value to the `bool()` built-in function, which accepts any input and
converts it to a Boolean. Add the following to your script:

```python
# All of these evaluate to False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))     # empty string
print(bool(()))     # empty tuple
print(bool([]))     # empty list
print(bool({}) )    # empty set (or dictionary)
```

This will become more relevant later, but it is mentioned here for completeness.

## Looking ahead

Next we will discuss `if` statements to leverage our knowledge of Booleans.