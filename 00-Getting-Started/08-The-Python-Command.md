# 8. The `python` command

In this section we will explore how to use the `python` command to run the Python
interpreter interactively. Later on, we will use the `python` command to interpret
code in source files.

## The `python` Command

Having installed Python with `rye`, we have access to the `python` command. We can use
`type` to find out where the command is located:

```bash
type -P python
```

On my system, I see:

```text
/home/sgarciat/.rye/shims/python
```

Notice that this is installed under the *hidden directory* (its name starts with a `.`)
called `.rye`, created automatically for us when we installed Rye. The Rye installation
modified our `PATH` to ensure programs in it can be found by the shell. This means if we
type `python`, our shell will recognize it:

```bash
python --version
```

This displays the Pythom version, such as:

```text
Python 3.12.5
```

Recall that command-line programs often provide a default behavior, and
may also accept command-line arguments or options that change that default
behavior. The `python` command is no different.

## Running Python Interactively: The Python REPL

If you run `python` with no arguments, like so:

```bash
python
```

Then, you will be presented with a welcome message and a *prompt*, similar to this:

```text
Python 3.12.4 (main, Jun  8 2024, 18:29:57) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Note that we no longer see the `bash` shell prompt (the `%` or `$`) because the
shell has transferred control over to `python`. Now instead we see `>>>`, which
is the Python prompt. Now it is Python (and not the shell) that pauses and
waits for us to provide input.

The environment we are in is sometimes called the **Read-Evaluate-Print-Loop**
or **REPL** for short, for the following reason:

1. **Read**: Python display a prompt such as `>>>` and pauses until you provide
a line of text and submit it with `ENTER`.
2. **Evaluate**: Python *parses* the line of text in order to determine if it
is valid Python syntax that it can therefore execute. If valid, it evaluates
the text as a Python command, possibly producing a value.
3. **Print**: Having completed its computation, Python may display a value,
such as the result of an expression or an error message.
4. **Loop**: The process starts all over. Python goes back to the beginning
step, and continues this way indefinitely (or until explicitly asked to stop).

This is not the first time you encounter a REPL: this is precisely what shells such
as `bash` do. Programs such as `bash` and `python` as often referred to as
*interpreters* because they evaluate a line of text at a time and immediately
execute it (as opposed to languages like *C* for which we must go through
a preliminary step known as *compiling*). As a result, the `python` program
is sometimes referred to as the **python interpreter**.

In spite of the similiarities, please keep in mind that `python` can only interpret
Python commands, and `bash` can only interpret Bash commands. For example,
here is what happens if you try to run the `bash` command `echo`:

```text
>>> echo "Hello world"
  File "<stdin>", line 1
    echo  "Hello World"
          ^^^^^^^^^^^^^
SyntaxError: invalid syntax
```

The `python` interpreter determined that `echo` is invalid and displayed an error
message to inform us. In Python, the way we produce text on the screen is with
the built-in `print()` function, like so:

```text
>>> print("hello world")
hello world
```

If you tried `print()` in `bash`, you would likely see an error as well,
because it is a Python command, not a `bash` command.

### Quitting the Python REPL

Recall that the L in REPL means to loop. How do we exit the loop? There's a few ways:

- Type the key combination `Control-D`: This produces a special character called **EOF**
or **End-of-file**. This tells Python that you will no longer provide any input, and
causes it to quit.

- Type `exit()` and press `ENTER`, which executes the built-in Python `exit()` command,
thereby quitting the `python` interpreter.

- Run the `quit()` function, similar to above.

Any of these will exit `python`, returning control to your `bash` shell. You will
no longer see the `>>>` prompt and will instead see yur regular shell prompt.

For more details, see [Using the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
in the official Python tutorial.

## Python Scripts

In computer programming, a **script** is a text file containing a sequence of commands written
in an interpreted language such as Python or Bash. To execute the commands in the file, we use a
special program called an **interpreter**, which executes each line one at a time. There are
many different computer languages with corresponding interpreters:

- Bash scripting and the `bash` interpreter
- JavaScript and the `node` interpreter (for NodeJS)
- Python and the `python` intepreter

Conventionally, a file meant to be interpreted by a specific program has a name and an extension that
indicates what type of script it is. For example, the `.py` extension is used to indicate that a text
file is a Python script. The term **scripting** often refers to writing computer code in an interpreted
language, such as Python.

### Creating a Python Script

Open your Terminal, and create an empty file as follows:

```bash
touch hello_world.py
```

The `touch` command updates the timestamp of a file, or creates the named file if it does not
already exist. Here, we chose the name `hello_world.py`. Notice that it has all lower case letters,
with an underscore `_` to separate the words, and the `.py` extension; this is standard, as we will
soon see. Now open the file with the `bash` command `open`:

```bash
open hello_world.py
```

Your default text editor should show up. In the file, type the following text:

```python
print("Hello, world!")
```

Save the file (optionally, close it), and head back to your terminal, where you will
type the following:

```bash
python hello_world.py
```

You should see:

```text
Hello, world!
```

Running `python` with `hello_world.py` as an argument instructs the Python interpreter
to interpret the commands in the text file a line at a time, effectively running
the code in it.

## Python REPL vs. Scripting

The REPL is useful when we wish to use Python interactively to learn the basics, try out
Python features, or run simple experiments. The downside is that if we exit the REPL and
come back, our work is lost. Moreover, typing Python code can be inconvenient for
complicated expressions.

The bulk of a programmer's time is spent scripting (and debugging), meaning writing
Python code in a text file. It's beneficial because you can save your code, modify it
easily, and share it with others. Also, there are many programs, such as *code editors*
and *integrated development environments* that enhance our programming workflow when we
use text files to write code.

To get a taste of Python from the REPL, see [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) on the official Python documentation.

## References

- [Using the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
