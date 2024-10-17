# Expressions

Python evaluates expressions to produce values. An **expression** may
include *literals*, *variables*, *function calls*, *operators*, and more.
Values may correspond to numbers, text, and collections of other values.
An easy way to explore expressions and values in Python is through the REPL
(Read-Evaluate-Print-Loop).

Open your Terminal, and then run the `python` command from your shell
to start up the REPL:

```bash
python
```

On my system, this looks like this:

```text
Python 3.12.6 (main, Sep 10 2024, 00:05:17) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Recall that `>>>` is the Python prompt, which you can see when running
Python interactively. For each of the following lines, type the expression
and press `ENTER` to run the command:

```python
0
-52
1 + 17
102 - 255
38 * (-48)
5.2 / 3.1
4 + 8j
"hello"
False
[5, 7, 0, -2, 23]
```

In my Terminal screen, this interaction looks like this:

```text
>>> 0
0
>>> -52
-52
>>> 1 + 17
18
>>> 102 - 255
-153
>>> 38 * (-48)
-1824
>>> 5.2 / 3.1
1.6774193548387097
>>> 4 + 8j
(4+8j)
>>> "hello"
'hello'
>>> False
False
>>> [5, 7, 0, -2, 23]
[5, 7, 0, -2, 23]
>>>
```

Python interprets each line and evaluates it. The REPL displays each value
onto the screen. In computer programming, another word for *displaying* content
as *output* on the screen, also known as *printing*.

If we include the same code in a Python script (a text file with Python code),
and use the `python` command to evaluate the file, Python will still evaluate
each line. However, unlike the REPL, Python will not display the value unless it
is explicitly told to.

To see this, let's create a Python script by using the `code` command in `bash`,
which should be available now that we have installed Visual Studio Code:

```bash
code expressions.py
```

Notice that we use `.py` as the extension to signify that this text file contains
Python code. Enter the same code from before:

```python
0
-52
1 + 17
102 - 255
38 * (-48)
5.2 / 3.1
4 + 8j
"hello"
False
[5, 7, 0, -2, 23]
```

To have `python` interpret your script, you can either click on the "Play" button
on the top-right in Visual Studio Code, which says `Run Python File`, or you can
issue the `python` command and provide it the filename as an argument on your shell,
like so:

```bash
python expressions.py
```

You will see no output whatsoever. Remember, Python did evaluate the commands. However,
it did not display their values because we did not ask Python to do so.
Next, we will learn how to use the `print()` function to display the value of expressions.
