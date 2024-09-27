# Strings

In Python, we use **strings** to represent text. Strings are of type `str`.

In Python, a string literal consists of characters delimited (enclosed) by one of:

- Single quotes: `'Hello, world!'`
- Double quotes: `"Hello, world!"`
- Triple single quotes: `'''Hello, world!'''`
- Triple double quotes: `"""Hello, world!"""`

The delimiters are not part of the strings, and only serves to inform Python
of what makes up the string.

## Basic Strings

Create a script called `strings.py`:

```bash
code strings.py
```

Type the following:

```python
print("Hello, world!")
print(type("Hello, world!"))
```

If you run this code, you will see the following in your terminal:

```text
Hello, world!
<class 'str'>
```

Notice that a string requires both an opening double quote `"` and a closing
double quote `"`. The text in between has the characters of the string.
We say that the string is *delimited* by double quotes (equivalently by
single quotes, or by triple quotes).

Notice that the quotes do not appear as part of the output. What if we wanted to
use quotes? If we are delimiting our strings with double quotes and want single
quotes in our message, then we can simply add them without an issue. Add
the following line of Python code to your script:

```python
print("That is Jane's bag.")
```

This will display:

```text
That is Jane's bag.
```

If we want to use double quotes, one choice is to use single quotes
to delimit the string, and double quotes inside the string. For example,
add the following line:

```python
print('They said it was "inappropriate", but I will take that as a suggestion.')
```

This will display:

```text
They said it was "inappropriate", but I will take that as a suggestion.
```

## Escape Sequences

Sometimes, we wish to display both types of quote in our string. What do we
do in that situation? This requires using what is called an *escape sequence*.
Type the following:

```python
print("They said \"wait a second, that's not yours!\" when it had my name on it.")
```

This will display:

```text
They said "wait a second, that's not yours!" when it had my name on it.
```

Notice the `\"`, which is a backslash followed by a double quote. This is called
an **escape sequence**, and it is valid to use within a string. When displayed
by `print()`, it is replaced by a double quote `"`. In general, escape sequences
consist of a backslash followed by another character:

- `\"`: A double quote.
- `\'`: A single quote.
- `\\`: A single backslash.
- `\t`: A tab character.
- `\n`: A newline character. This causes the following text to be displayed on
the next line.

Here's an example of using `\n` and `\t`. Add the following to your script:

```python
print("Dear Professor,\n\n\tI'm excited to \"ace\" this class.\n\nSincerely,\nStudent")
```

The result is the following:

```text
Dear Professor,

        I'm excited to "ace" this class.

Sincerely,
Student
```

## Multiline Strings

To write a message that spans multiple lines, we can use the `\n` escape sequences,
but that can get difficult. Instead, we can delimit our strings with three single
quotes or three double quotes.

Add the following to your Python script:

```python
print("""Dear Professor,
      
    I'm excited to "ace" this class.
      
Sincerely,
Student""")
```

This will display the same as before without using `\n` or `\t`:

```text
Dear Professor,
      
    I'm excited to "ace" this class.

Sincerely,
Student
```

## Format Strings

**Format strings**, or **f-strings**, are a convenient provided by Python
to format messages easily. To see them in action, add the following code
to your script:

```python
# Calculate the area of a rectangle of known dimensions
width = 8
height = 15
area = width * height

# Create a message using a format string.
print(f"A rectangle of width {width} and height {height} has area {area}.")
```

You will see:

```text
A rectangle of width 8 and height 15 has area 120.
```

Notice that we add the single character `f` in front of the opening string
delimiter (before the string delimiter, in this case a double quote). This
makes our string a format string. This enables use to use curly braces `{}`
inside the string, and to place Python expressions inside them. Python will
replace the curly braces and the expression with characters in the string
representing the result.

For example:

- `{width}` is replaced with `8`.
- `{height}` is replaced with `15`.
- `{area}` is replaced with `120`, the result of `width * height`.

Any valid Python expression is allowed in the curly braces when using
a format string, not just variables.

A neat shortcut when you wish the message to contain the variable's name
is to add the `=` sign as a suffix in the variable name within the braces `{}`.
Add the following to your script:

```python
# A shortcut when you want the variable name in the message
print(f"A rectangle of {width=} and {height=} has {area=}.")
```

This will display:

```text
A rectangle of width=8 and height=15 has area=120.
```

## String Methods

In Python, a *method* is a function that can be invoked by using
the *dot notation*. Recall we used the math module before, like so:

```python
import math

math.gcd(5, 3)
```

Here, `gcd()` is a method provided by the `math` module by using
the dot notation.

Similarly, strings have many methods at their disposal. Given a
string `s`, we have:

- `s.upper()`: Produce an uppercase version of `s`.
- `s.lower()`: Produce a lowercase version of `s`.
- `s.capitalize()`: Produce a string whose first letter is capitalized if it
is the first character in the string. If the first character is not a letter,
does nothing. Capitalize only the first character in `s` (and only if its a letter).
- `s.title()`: Produce a string for which all letters are in lowercase, except
the first letter of each "word". Here, "words" are separated by whitespaces.
- `s.lstrip()`: Produce a string with the initial whitespace characters removed.
- `s.rstrip()`: Produce a string with the ending whitespace characters removed.
- `s.strip()`: Same as applying both `lstrip()` and `rstrip()`. Notice that
spaces within the string, not at the end or at the beginning, are preserved.
- `s.removeprefix(my_prefix)`: Produce a string equivalent to the first, except
that if the sequence of characters given by `my_prefix` exists at the beginning
of `s`, then they are not in the resulting string.

Note that I was careful to say "produce a string..." rather than "change the string".
In Python, strings are **immutable**, meaning that they never change. So if
`s` is a variable (label) for the string `"Hello"`, then that string `"Hello"` will
never change, even if you call methods on it. Notice that `s` may be reassigned to
refer to a different string, which is allowed.

Add the following to your script:

```python
message = "   Hello, world    "
print(message)
print(message.lower())
print(message.upper())
print(message.title())

print(message.rstrip())
print(message.lstrip())
print(message.strip())

HOME_PAGE = "https://www.linkedin.com/in/sergio-garcia-tapia/"
print(HOME_PAGE.removeprefix("https://"))
```

You should see:

```text
   Hello, world    
   hello, world    
   HELLO, WORLD    
   Hello, World    
   Hello, world
Hello, world    
Hello, world
www.linkedin.com/in/sergio-garcia-tapia/
```

Since strings are immutable, and `message` and `HOME_PAGE` were never
reassigned, we can show that they still hold their original value.
Add the following line:

```python
print(f"Values at the end: {message=}, and {HOME_PAGE=}")
```

You should see:

```text
Values at the end: message='   Hello, world    ', and home_page='https://www.linkedin.com/in/sergio-garcia-tapia/'
```

## The `len()` built-in function

Another useful function which is not a string method but can be applied
to strings is the `len()` built-in function. When applied on a string
`s`, the value of `len(s)` is the number of characters in `s`.

Add the following to your script:

```python
print(f"The string {message=} has {len(message)} characters")
print(f"The string {HOME_PAGE=} has {len(HOME_PAGE)} characters")
```
