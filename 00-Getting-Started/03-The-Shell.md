# 3. The Shell

## What is a shell?

A **shell** is a program whose job is to interpret lines that you enter (usually with your
keyboard) to run programs that you requested, and to coordinate what happens between you
and the operating system. Shells are programs like any other, but because of their unique
role, it almost feel like the shell itself is the operating system.

Most shells are based on Unix, and there are many variants:

- The original UNIX shell was the **Bourne Shell** named after its creator Steven Bourne.
Since then, many derivatives have sprung up. In most systems it appears as the program with
name `sh`.

- The **Bourne Again Shell** (often called **bash**) was created by the *GNU project*, an
open-source software movement by software enginer and activist Richard Stallman.
The corresponding program name is `bash`, and it is commonly the default shell in
GNU/Linux-based distributions such as Ubuntu, Raspbian (the OS for a Raspberry Pi),
Fedora, and more.

- The **Z Shell** is a modern alternative that is commonly the default in macOS
systems. The corresponding program name is `zsh`, and it is based on the Bourne Shell too,
including some features from `bash` and other shells.

## Using your Shell through a Terminal Application (macOS)

There are many of ways to [open a terminal on Mac](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac#:~:text=Click%20the%20Launchpad%20icon%20in,%2C%20then%20double%2Dclick%20Terminal.).
One way is:

- CLick the Launchpad icon in the Dock.
- Type `Terminal` in the search field.
- Click `Terminal`.

The terminal window will display some text, and a `%`, which is called a *shell prompt*.
We can type text that names a valid *command* to produce useful information.

## Identifying our Shell

For example, we can find our what shell your terminal is running by entering the
following text exactly (mind the lower and uppercase):

```bash
echo $SHELL
```

After pressing `enter` (or `return`), you will see text similar to:

```text
/bin/zsh
```

or perhaps

```text
/bin/bash
```

Let's dissect this command:

- `echo` is the name of a command. It accepts input, and displays it back on the screen
(like yelling in a cave and hearing the echo).

- `SHELL` is a *shell variable*. When prefixed by a `$`, the shell *expands* (replaces)
`$SHELL` with a *filesystem path* (a location in our computer) of the shell program we
are running.

To summarize, your shell replaces `$SHELL` with the the path `/bin/zsh` (or `/bin/bash`, or
something similar), the `echo` commnd accepts it as input, and then it displays it to
us on the screen as output.

A computer system typically has a default shell, but may also ship with many shells. To
see what shell programs are avaiable in our system, we can inspect a file whose
filesystem path (location in our computer) is `/etc/shells`. To display the contents
of a file on a terminal screen, we can use the `cat` command:

```bash
cat /etc/shells
```

On my computer, the output looks something like this:

```text
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/sh
/bin/dash
/usr/bin/dash
```

You can see I have `sh`, `bash`, and others. The list on your computer may be different.
macOS ships with both `bash` and `zsh`. Regardless of the default shell in your system,
we will focus on `bash`, so we will discuss how to change the default. Unfortunately, due
to licensing reasons, the `bash` version that ships with macOS is very old, so it is not
suitable for the work we will do. We will begin by installing an up-to-date version of `bash`,
and then making it our default shell.

## References

- [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
- [Zsh](https://en.wikipedia.org/wiki/Z_shell)
