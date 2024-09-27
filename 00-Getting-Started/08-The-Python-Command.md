# 8. The `python` command

Now that we have installed Python, we can use the `python` command, and we can begin
learning Python in earnest. We will begin by learning how to use the Python REPL to
run simple commands and learn the basics. Later, we will run Python by storing Python
in a file.

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

Recall that command-line programs often provide a default behavior, and may also accept command-line arguments or options that change that default behavior. The `python` command
is no different.

## The Python REPL

If you run Python with no arguments, like so:

```bash
python
```

Then, you will be presented a prompt similar to this:

```text
Python 3.12.4 (main, Jun  8 2024, 18:29:57) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is a *prompt*, which is how Python indicates that it's waiting for you to provide
it input. This environment is called the **Python REPL**, which stands for
*Read-Evaluate-Print-Loop*. It's named this way because Python will read your command,
will evaluate it to determine whether it's valid before attempting to run it, will display
the result, and then starts all over again (loop).

The `python` program is sometimes synonymously referred to as the **python interpreter**,
because it interprets text you enter as commands (or code) to execute (run). This should
remind you of your shell, which does the same:

1. **Read**: Waits for you to type a command. Typically a prompt such as `>>>` is shown by Python, or `$` for a shell, or something else depending on the interpreter.
2. **Evaluate**: Evaluates the command you type to make sure it is valid, and runs it.
3. **Print**: Displays the result of running the command.
4. **Loop**: Start over.

The difference is your shell interprets *shell commands* and Python interprets
*Python commands*. Therefore, using the `echo` command, for example, will not work:

```text
>>> echo "Hello world"
  File "<stdin>", line 1
    echo  "Hello World"
          ^^^^^^^^^^^^^
SyntaxError: invalid syntax
```

On the other hand, whereas `echo "hello world"` displays text while in your shell,
the following does the same in Python:

```text
>>> print("hello world")
hello world
```

The difference is that `echo` is a shell command, whereas `print()` is a Python
command (or function). The parentheses are necessary, because `print` is a *function*,
and in Python we use parentheses `()` to execute a function.

### Quitting the Python REPL

The first thing we should learn is how to exit. We can do so in a few ways:

- Type the key combination `Control-D`: This produces a special character called **EOF** or **End-of-file**. This tells Python that you will no longer provide any input, and causes it to quit.

- Run the `exit()` command (similar to above).

- Run the `quit()` function (include the parentheses, and no spaces).

Any of these will exit Python and return you to your regular shell prompt, where now it is your
shell, and not Python, that waits for a command.

For more details, see [Using the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html) in the official Python tutorial.

## Python Scripts

In computer programming, a **script** is a text file containing a sequence of commands written
in an interpreted language such as Python or Bash. To execute the commands in the file, we use a
special program called an **interpreter**. There are many different computer languages with
corresponding interpreters:

- Bash scripting and the `bash` interpreter
- JavaScript and the `node` interpreter (for NodeJS)
- Python and the `python` intepreter

Conventionally, a file meant to be interpreted by a specific program has a name and an extension that
indicates what type of script it is. For example, the `.py` extension is used to indicate a text file
is a Python script. The term **scripting** often refers to writing computer code in an interpreted
language, such as Python.

### Creating a Python Script

Open your Terminal, and create an empty file as follows:

```bash
touch hello_world.py
```

The `touch` command updates the timestamp of a file, or creates the named file if it does not
already exist. Here, we chose the name `hello_world.py`. Notice that it has all lower case letters,
with an underscore `_` to separate the words, and the `.py` extension. Now open the file for
editing:

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
to interpret the commands in the text file, effectively running your code.

## Python REPL vs. Scripting

The REPL is useful when we wish to use Python interactively to learn the basics, try out
a Python feature, or run simple experiments. The downside is that if we exit the REPL and
come back, our work is lost, and typing Python code can be inconvenient.

The bulk of a programmer's time is spent scripting, meaning writing Python code in a text file.
It's beneficial because you can save your code, modify it easily, and share it with others.
Also, there are many programs, such as *text editors* and *integrated development environments*
that enhance our programming workflow when we use text files to write code.

To get a taste of Python from the REPL, see [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) on the official Python documentation.

## References

- [Using the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
