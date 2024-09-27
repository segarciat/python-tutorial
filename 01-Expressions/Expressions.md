# Expressions

Python evaluates expressions to produce values. An **expression** may
include *literals*, *variables*, *function calls*, *operators*, and more.
Values may correspond to numbers, text, and collections of other values.
An easy way to explore expressions and values in Python is through the REPL.

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
Python interactively through the REPL. Type the following, each on its
own line (by pressing) `enter`:

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
out to the screen (also  known as displaying output) is called *printing*.

Outside the REPL, Python will still evaluate each line, but it will not display
the value unless it is explicitly told to. To see this, let's create a Python
script by using the `code` command in `bash`, which should be available now that
we have installed Visual Studio Code:

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

Now using Python to execute the code in the script by either using the button that
says `Run Python File` in VS Code, or by issuing the following command to your shell
via your terminal:

```bash
python expressions.py
```

You will see no output whatsoever. Python did evaluate the commands, but it did not
display any output. Next, we will learn how to use the `print()` function to display
the value of expressions.
