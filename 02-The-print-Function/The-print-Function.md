# The `print()` Function

In the previous section, we saw that the REPL will evaluate expressions such
as `3 + 14` and diplay the result. However, when we placed such as line in
our script and ran it, we did not see any output. In this section, we will
explore the built-in `print()` function, whose job is to output values of
expressions.

Begin by creating a file called `printing.py`:

```bash
code printing.py
```

Now add the following content:

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

Run it with Visual Studio Code, or use the `python` command on your file:

```bash
python printing.py
```

You should see:

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

The output is equivalent to what we saw when we ran each line separately
in the REPL. Let's discuss what happened:

1. When we ran `python printing.py`, Python noticed that we provided
a filename. Therefore, it did not start the REPL environment.

2. The `python` interpreter opened `printing.py` and began at the first
line, containing `print(0)`, and began interpreting the text as Python
code.

3. Python recognized `print()` as an invocation of a built-in function
that displays output. It sees the `0` inside the parentheses, and
it determines it must output `0` on the screen.

4. Python moves on to the next line and repeats the process.

## What is a function?

Simply, a *function* is a named computation encapsulates a
useful computation that can be reused. Functions often accept
inputs and produce outputs. This should remind you of functions
in mathematics, such as a polynomial $f(x)=x^2$ which, given
an input value $x$, it produces the its square $x^2$.

For concreteness, consider the line with `print(1 + 17)`.
This is how we tell Python that we wish to use the function,
and it consists of the following parts:

- The name of the function, which is `print`.
- A balanced set of parentheses `()`, which is used to signify that we
are *calling* or *invoking* the *print* function. There must not be
a space between the function name (`print`) and the parentheses `()`.
That is, we must write `print()`,  not `print ()`.
- An *argument* inside the parentheses, here `1 + 17`. Note `print()`
does not evaluate the computation `1 + 17` as `18`. Rather, Python
does this on behalf of `print()`, gives the result to `print()`,
and then `print()` displays `18` to the screen.

As you can see, the `print()` function in Python is similar to the `echo`
command provided by your shell, but please note that `echo` is not
directly accessible within a Python program, and `print()` is not
directly accessible from the shell.

Like many other functions, `print()` accepts more than one argument, or
even no arguments at all! If given no argument, `print()` will output
a blank line. To give it more than one argument, separate each one by a
comma. To try it, add the following lines to the end of `printing.py`:

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

## Comments

You may have noticed lines that begin with `#` in the previous example. In Python,
lines that begin with `#` are known as **comments**. Python ignores comments,
meaning that it will not attempt to interpret them as code, thereby allowing you
to type whatever you want. Comments are useful when you wish to explain your
thought process, or to plan out how you will approach the problem you are trying
to solve. In this tutorial, I will liberally use comments to explain what
certain lines of codes do.

## References

- [List of Python Built-in Functions](https://docs.python.org/3/library/functions.html)
