# The `print()` Function

In Python, a function represents logic with a well-defined interface and
behavior and can be invoked multiple times. We will talk more about functions
later, but of immediate interest is the *print* function.

The purpose of the *print* function is to display textual output, normally to
a terminal screen, but possibly to a file. Going forward, I will refer to
functions using parentheses, such as `print()`, because parentheses are
used to invoke functions. This also helps to distinguish them from variable
names, which we will discuss later. `print()` is a built-in function, meaning
that it is provided with Python. We will encounter many other such functions
later, as well as other functions that are not built-in.

Create a Python script called `printing.py`:

```bash
code printing.py
```

Add the following code:

```python
print(0)
print(-52)
print(1 + 17)
print(102 - 255)
print(38 * (-48))
print(5.2 / 3.1)
print(4 + 8j)
print("hello")
print(False)
print([5, 7, 0, -2, 23])
```

Now run it, and you will see:

```text
0
-52
18
-153
-1824
1.6774193548387097
(4+8j)
hello
False
[5, 7, 0, -2, 23]
```

The `print()` function has three components:

- The name of the function, which is `print`.
- A balanced set of parentheses `()`, which is used to signify that we
are *calling* or *invoking* the *print* function. There must not be
a space between the function name (`print`) and the parentheses `()`.
That is, we should write `print()`,  not `print ()`.
- An *argument* inside the parentheses. The argument is an expression.
In the example above, we used many different expressions.

As you can see, the `print()` function in Python is similar to the `echo`
command provided by your shell.

Like many other functions, `print()` accepts more than one argument, or
even no arguments at all! If given no argument, `print()` will output a blank
line. To give it more than one argument, separate each one by a comma. To try it,
add the following lines to the end of `printing.py`:

```python
print("Hello world!")
print()
print("Goodbye", "world")
```

When you run the script, you should see the following lines towards the end:

```text
Hello world!

Goodbye world
```

When you use a comma (`,`) to pass more than one argument to `print()`, the value
of each argument is displayed on the screen, and they separated by one space from
one another (by default).

We will return to the `print()` command throughout our study.

## References

- [List of Python Built-in Functions](https://docs.python.org/3/library/functions.html)
