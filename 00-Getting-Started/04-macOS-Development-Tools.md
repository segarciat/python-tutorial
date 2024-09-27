# 4. macOS Development Tools

Out of the box, a macOS computer may not contain all of the software and tools needed for
being able to write computer programs effectively. Fortunately, Apple provides a separate
development environment for programmers named *Xcode*. Our main goal in this section is to
install [Homebrew](https://brew.sh/), and in the process, we will install Xcode.

An excellent resource with guides on installing macOS software is
[mac.install.guide](https://mac.install.guide/) by Daniel  Kehoe. I will attempt
to summarize the details, but if you encounter difficulties, I encourage you to check
out their guides.

## Installing Homebrew

[**Homebrew**](https://brew.sh/) is a package manager for macOS. A **package manager** is
a program used to install other programs through your shell. I will provide an overview of
the necessary steps to install Homebrew, but see [Installing Hombrew on mac.install.guide](https://mac.install.guide/commandlinetools/3) for details.

Begin by opening your `Terminal` application so that we can type shell commmands.
Then, enter the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Here are some notes:

- `/bin/bash` is the path to the `bash` program in your system, by naming it first,
we are telling our shell to use it to interpret commands for us. The `-c` is an example
of a *command-line option*, which alters the default behavior. In this case, it tells
`bash` to run the command in double quotes.
- Inside the double quotes `"` we have a command that is to be interpreted by `bash`.
Namely, the `curl` command is used for data exchange between devices. In this case,
we are downloading the file whose URL we are providing. The `-fsSL` are command-line
options that `curl` understand, and you do not need to concern with them at the moment.

When you run the command, the Homebrew installation will begin within your terminal:

- Enter your `password` when prompted. This is normally necessary to install a
program no your system.
- You will see a list of files that Homebrew will install. If you see a message
about XCode Command Line Tools, be sure to accept it by pressing `return` (or `enter`)
when prompted.
- Homebrew may display instructions about modifying your `PATH` shell variable by
editing your `~/.zprofile` file to ensure  your shell knows where to find it when you
write the command name.

As a reminder, be sure to checkout [Installing Hombrew on mac.install.guide](https://mac.install.guide/commandlinetools/3) if you run into difficulties.

If successful, you should be able to use the `brew` command (not `homebrew`).
To verify this, type the following:

```bash
brew doctor
```

Ideally, this will display something similar to:

```text
Your system is ready to brew.
```

## References

- [Homebrew](https://brew.sh/)
- [Installing Hombrew on mac.install.guide](https://mac.install.guide/commandlinetools/3)
