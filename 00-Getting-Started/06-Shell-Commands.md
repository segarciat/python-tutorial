# 6. Running Commands on your Shell

Our focus is to learn Python. However, at times, we will find it necessary, and even helpful, to run commands on your shell. For example, we have ran several commands so far:

- `echo` to display text in the screen (in our case, the value of shell variables).
- `cat` to display the content of text files.
- `brew` to install an up-to-date version of `bash`.
- `open` to open a file.

We will also use many other commands, such as `cd`, `ls`, and `less`. When we install
Python, we will also use the `python` command to execute our Python programs.
This list of commands is non-exhaustive since there are so many. There is no need
to memorize them because we can always use a browser to learn more about them.
However, there's a few that is often handy to remember.

The focus here will be on `bash`-specific commands. To make sure you are running `bash`:

```bash
echo $SHELL
```

The output should be something like:

```text
/opt/homebrew/bin/bash
```

If not, see one of the previous documents for instructions on how to make it the
default, or find help online.

## What is a Command?

A **command**  can mean several things:

- A *executable program*, located somewhere in our system, named by a single word. Examples include `ls` to list files in our current directory, `cat` to display content in files, `date` to display the current date, `find` to look for a specific file in your filesystem, and so on.

- A *shell built-in*, which is part of the shell program. For example, the `cd` command to change directories, the `pwd` to see the directory we are currently in, the `echo` command to display text, `type` to inspect what type of command we are dealing with.

- A *pipeline*, where we combine many commands into one, typically using the *pipe*
symbol `|`.

## Invoking a Command: `pwd`

To invoke a command, we type its name, and press `enter` (or `return`) at the terminal.
As an example, type the following command:

```bash
pwd
```

`pwd` stands for "print working directory". The `pwd` command answers the simple question
"what is the current location of the shell program we are running under our terminal?"
On my Ubuntu system, it displays:

```text
/home/sgarciat
```

If I were on a macOS, it might show instead:

```text
/Users/sgarciat
```

This is an example of a filesystem path, or just path.

## Filesystems and paths

A **filesystem** is a hierarchy consisting of *directories* (folders) and *files*. A *directory* is simply a container for other files and directories. On macOS, you can see
your files and directories by using the **Finder** application. Some examples of directories are `Downloads`, `Desktop`, `Documents`, and so on. The **root directory**, with name `/` (forward slash or just slash) is your top-most directory. That is, every other file and
directory in the hierarchy is contained somewhere under it.

A **filesystem path**, or just **path**, represents a location for a file, program,
directory, etc, in your computer. Typically, it consists of names separated by
a *filesystem separator*, typically a forward slash `/` on UNIX-based systems such
as macOS. A path describes the list of directories that you must traverse to reach the
destination of the file or directory.

For example, `/Users/sgarciat` is a path to my *home directory*. To get there, I start
at the root directory `/`, descend into the `Users` directory, and finally, into  the
`sgarciat` directory. This is an example of  an *absolute path*, because it starts at the
root directory `/`, but we can have *relative paths*, which begin with either the name
of a a file or directory located under current directory (whose path we can see with
`pwd`), or with a `.` (or two dots `..`).

If we were  using the `Finder` application on macOS, "descending" into each directory
would entail clicking the folders that we see in the window. As we will see, to do this
in the command-line, we use the `cd` (change directory) command.

## Viewing Files and Directory: `ls`

The `ls` command displays the list of files stored at the current path:

```bash
ls
```

On my system, the output looks something like this:

```text
code        Downloads   Videos      Desktop bin
Documents   Pictures    Screenshots todos.txt
```

This should match what you see with your **Finder** application, more or less.

## Changing Directories: `cd`

We can explore the file system by moving around with the `cd` command, which stands for
*change directory*:

```bash
cd Documents
pwd
ls
```

Here I ran three commands:

- `cd Documents` to navigate into `Documents` directory (similar to clicking `Documents`
in **Finder**). Here, `Documents` is called an *argument* or *parameter* of the `cd` command;
it tells it specifically what to do (where to go).
- `pwd` prints (displays) the updated path of our working (current) directory, which has
changed because of the `cd` command. For example, if it was `/Users/sgarciat` before,
it will now be `/Users/sgarciat/Documents`.
- `ls` displays the files and directories under our current working directory.

What if we wish to go back? We can say:

```bash
cd ..
pwd
```

The `..` stands for *parent directory*, meaning the directory containing this one.
This means we go back to our home directory, assuming that is where we started.
As another alternative, suppose that we start at our home directory and navigate
into the `Downloads` directory:

```bash
cd $HOME
cd Downloads
pwd
ls
cd
```

The last command, `cd`, was written all by itself; no arguments! By default, `cd` returns
us to our home directory, no matter where we are on the file system. This is neat for
when you get lost. Another option is:

```bash
cd ~
```

The `~` is short for your home directory, and you'll often use it and see it. As you
probably guessed, `cd $HOME` is yet another way to do the same thing.

## Shell Variables

The behavior of your shell is affected by pre-configured *shell variables*. In computer
programming, **variable** is a label for a value. To view represented by a shell variable,
use the `printenv` command (or `env`, try both and see which one works). For example,
let's look at the `HOME` variable:

```bash
printenv HOME
# or try...
# env HOME
```

This should display the path to your home directory. This is how your shell knows
where to navigate when you type `cd` or `cd ~` or `cd $HOME`. Another way to view the
value of a shell variable is by prefixing it a dollar sign  `$` and using the `echo`
command:

```bash
echo $HOME
```

Unlike the `printenv` command, the `$` is necessary because the `echo` command is
not responsible for determining the value of the `HOME` variable. Rather, the shell
sees the dollar sign `$` in front `HOME`, and then it replaces `$HOME` with your home
path before passing it as an input to the `echo` command. Then `echo` displays the path.

To see all of your currently set shell variables, type `printenv` (or `env`) without any arguments:

```bash
# or...
# env
printenv
```

There's probably a lot! We don't care about most of them. To clear your screen, use
the `clear` command:

```bash
clear
```

You can also press the key combination `Control-L` on your keyboard to clear your text
(not `Command-L`).

Some examples of variables are:

- `HOME`: Contains the path to your home directory.
- `USER`: Contains your username.
- `SHELL`: Contains the path to the shell you are currently using.
- `PATH`: Contains a list of paths where your system searches when you ask it to run a command.

## The `PATH` Variable and the `type` Command

Among all the variables that exist, `PATH` is one of the most important. To view its contents, run:

```bash
echo $PATH
```

Its exact contents differ from one computer to the next, but its format is generally the same.
On mine, it looks like this (I have shortened it for simplicity):

```text
/home/sgarciat/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/usr/local/games:/snap/bin
```

It is a list of paths, delimited by (separated by) colons `:`. To see each path in its own line
you can provide the output of `echo` as an input to the `tr` command (in short, *pipe it*):

```bash
echo $PATH | tr : "\n"
```

The `tr` command replaces each instance of the first character it receives (here `:`) with an
instance of the second character it receives (here `"\n"`, which is the newline character).
For the paths above, the output is:

```text
/home/sgarciat/bin
/usr/local/sbin
/usr/local/bin
/usr/sbin
/usr/bin
/usr/local/games
/snap/bin
```

When you type a command such as `ls`, `cat`, or `pwd`, or `echo`, your shell does something like this:

1. If the command is a built-in like `pwd`, `echo`, or `type`, it does not need to look anywhere; it's part of the shell,
so it can run it  immediately.
2. If the command is not a built-in, then it's likely an *executable program*, and its *binaries* (the files with machine code and instructions to run the command/program) are located somewhere. It must find these file with instructions to run the command.

The latter of these two cases is where `PATH` matters. The list of paths is where your shell searches for the command.  Is `ls` at `/home/sgarciat/bin/ls`? If not, keep searching, until it finds it, and it finally runs it, or displays an error
message saying that it failed.

A simple way to find out whether a command is a shell built-in or a program (and in this case, where its binaries are) is by running the `type` command. Try these:

```bash
type -P ls cat date
```

On my system, the output is something like this:

```text
/usr/bin/ls
/usr/bin/cat
/usr/bin/date
```

The `-P` is a command-line option, which we will discuss shortly. In brief, it instructs the `type` command to display the paths of the commands we name. As you can see, the  binaries for each of these three are located in the `/usr/bin` directory in my system.

## Components of a Command

Now that we have run a few commands, let's talk about the parts of a command. A command
generally has the following form:

```text
command_name [options] arguments
```

- **Command name**: Every command has a name, which has no spaces, and typically contains only letters (but it may contain underscores, numbers, or some other characters). For example, we've seen `pwd`, `echo`, `cat`, `ls`, `date`, `type`, etc.

- **Options**: A command-line option alters the default behavior of a command. Typically, we use a dash `-` followed by a letter to specify an option. For example, we use the `-P` option of the `type` command in the previous section. Some commands allow us to specify more than one option. Options are not always required (hence the name). Some programs also use two dashes `--`, such as `ls --help`, to allow you to provide the option in an equivalent but more verbose "long form".

- **Arguments**: A command may accept (or even require) arguments. These indicate what the command will operate on, or information that it needs in order to run. For example, `cd Documents` tells the `cd` command that we wish to navigate to the `Documents` directory. Or, `type date` tells the `type` command that we want information about the `date` command.

Here are some examples with the `ls` command

```bash
# List information about files in full detail, such as permissions and modification dates
ls -l

# List hidden files, which often begin with a dot .
ls -a

# Do both!
ls -la

# Show me detailed information about files in my Downloads folder, including hidden files
ls -la Downloads

# Help informtion about the ls command
ls --help
```

The `wc` command stands for "word count", and it can be used to know how many lines, words, and
characters are in a line. By default, it shows all three, but we can limit what it shows by passing
command-line options:

```bash
# View contents of /etc/shells
cat /etc/shells
# How many lines, words, and characters are in the file named /etc/shells
wc /etc/shells

# Only show me how many lines
wc -l /etc/shells

# Only show many how many words
wc -w /etc/shells
```

## Obtaining Help

How we can we find out  what options are available for a command, or more generally, how to use a command? One simple way would be to browse the web. We can also find out from the command line instead.
To determine what to do, we first use the `type` command with the `-t` option to see if it's a built-in command or a binary:

- `builtin`: When `type` displays this, we should use the `help` command to find out more, such as `help echo`.
- `file`: This means it's an executable program (a binary), so we can try the `-h` option or `--help`.

For example, `cd` and `pwd` are shell built-ins, so we can use the `help` commmand:

```bash
type -t cd pwd
help cd
help pwd
```

Interestingly, `type` is a command too, so we can use it on itself; it's actually a built-in:

```bash
type -t type
help type
```

If we type `help`, we see the full list of built-in commands:

```bash
help
clear
```

For a binary like `cat` or `ls`, use `--help`:

```bash
type -t cat ls
cat --help
ls -h
```

## Viewing Information Convenient with `less`

The `--help` option and the `help` command display a lot of information. We can *pipe it* into the `less` command to view it a page at a time:

```bash
ls --help | less
```

You can press your Enter key, or up and down arrows to scroll through. When you are done, press the `q` key on your keyboard. You can even use `less` to view the contents of a file:

```bash
less /etc/shells
```

Typically, the help text display a "Usage" message with the command name, possibly square brackets `[]`, and ellipses `...`,
like if we  run:

```bash
# It's a program...
type -t  wc

# So we can try --help
wc --help
```

we see

```text
Usage: wc [OPTION]... [FILE]...
```

The square brackets indicate that `OPTION` (described throughout the rest of the help text displayed) is,
well, optional! Thatis, it's not necessary to provide it for the program to function. The combination `[OPTION]...`
means "you can provide more than one option". Of course, if no options are required, then there is some default
behavior we need to be familiar with.

## More Information

Checkout these resources to learn a little more.

- [Getting started with bash](https://academind.com/tutorials/terminal-bash-basics)
- [Filesystems and paths](https://education.launchcode.org/intro-to-web-dev-curriculum/terminal/reading/filesystems-paths/index.html)
- [List of Popular Commands](https://www.hostinger.com/tutorials/linux-commands)
- [PATH Variable](https://www.namehero.com/blog/understanding-what-the-linux-path-variable-is-and-how-to-add-to-it/): Warning, do not attempt to change your `PATH` variable. We will learn how to safely do this later.
