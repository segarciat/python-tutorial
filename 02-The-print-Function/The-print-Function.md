# The `print()` Function

In the previous section, we saw that the REPL will evaluate expressions such
as `3 + 14` and diplay the result. However, when we placed such as line in
our script and ran it, we did not see any output. In this section, we will
explore the built-in `print()` function, whose job is to output values of
expressions.

In Python, a *function* is a named operation a well-defined interface and
behavior that can be invoked multiple times. A function may accept inputs
and perform an operation that may display output.

It is similar to an *operator* such as the addition operator `+`, which takes
inputs and produces outputs. For example, in `3 + 14`, the inputs as
`3` and `14`, and the output is `17`, the result of the operation.
We will talk more about functions later, but of immediate interest is the
*print* function.

The purpose of the *print* function is to display textual output, normally to
a terminal screen, but possibly to a file. Going forward, I will add the
parenthesis pair `()` as a suffix to functions, such as `print()`, because
parentheses are used to *call* (to action) or *invoke* functions. This also
helps to distinguish them from variable names, which we will discuss later.

`print()` is a built-in function, meaning that it is provided with Python.
We will encounter many other built-in and non built-in functions later.

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

Here, Python evaluated each expression inside the parentheses,
passed the result to `print()`, and invoked `print()` to display
the result.

The function call `print(-52)` function has three components:

- The name of the function, which is `print`.
- A balanced set of parentheses `()`, which is used to signify that we
are *calling* or *invoking* the *print* function. There must not be
a space between the function name (`print`) and the parentheses `()`.
That is, we should write `print()`,  not `print ()`.
- An *argument* inside the parentheses. The argument is an expression,
and is what `print()` will display to the screen. In the example above,
we used many different expressions. For example, `-52` is an argument.

As you can see, the `print()` function in Python is similar to the `echo`
command provided by your shell, but please note that `echo` is not
directly accessible within a Python program, and `print()` is not
directly accessible from the shell.

Like many other functions, `print()` accepts more than one argument, or
even no arguments at all!
If given no argument, `print()` will output a blank
line. To give it more than one argument, separate each one by a comma. To try it,
add the following lines to the end of `printing.py`:

```python
# One argument: displays its value and ends with a newline
print("Hello world!")
# Displays no text and a newline
print()
# Displays Goodbye and world, separated by a single space, and a newline
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
