# 05 Making `bash` your Default macOS Shell

Recall that computer systems often ship with many shells. For example, macOS systems
ship with `zsh` and `bash`. Though `zsh` is an excellent shell, we will prefer `bash`.
`bash` ships with macOS at the path `/bin/bash`, but it is very old version, not suitable
for daily use. In what follows, we will show the steps necessary to install `bash` with
Homebrew. Then we will make it our default shell.

I drew the steps from [this video walkthrough on making `bash` the default macOS shell](https://www.youtube.com/watch?v=AWQ7LNT9vME). In what following, I will attempt to summarize,
but please refer to that clip for details.

## Installing an up-to-date Version of `bash`

Begin by opening your `Terminal` application so that we can interact with the shell.
Previously we installed Homebrew to use as a package manager, so we will use it to
install an updated version of `bash`. Type the following command exactly:

```zsh
brew install bash
```

Depending on whether your computer has an Intel chip or an Apple Silicon chip, it will have installed to one of the following:

- **Intel**: `/usr/local/bin/bash`.
- **Apple Silicon**: `/opt/homebrew/bin/bash`.

Try both of these commands

```zsh
/usr/local/bin/bash --version
/opt/homebrew/bin/bash --version
```

We will proceed under the assumption that `/opt/homebrew/bin/bash` is the installation
location. However, modify the steps according your specific case. Copy this filesystem
path to a text file so that we can use it later.

## Changing Default Shell to `bash`

We want to ensure that bash is our default shell:

1. With your `Terminal` application open, click `Preferences`, by clicking the Apple Logo
on the top left of your screen.
2. In the window that opens, go to `General`, and navigate to where it says `Shells open with:`.
3. Click the `Command (complete path):` radio button, and type or paste the path you copied
earlier. For example, if you are on Apple Silicon, type or paste `/opt/homebrew/bin/bash`.

Now close your `Terminal` application, and open a new instance of it. It should now
show that `bash` is your default shell. However, we must do more, because if we type

```bash
echo $SHELL
```

it may still say `/bin/zsh`. We will use the *change shell* command. Let's first add
our newly installed version of `bash` located at `/opt/homebrew/bin/bash` to the list
of valid shells:

Run the following to open `/etc/shells`:

```bash
sudo open /etc/shells
```

The `sudo` command stands for *superuser do*, and it is a command needed to perform administrative and privileged tasks. Requiring `sudo` is a safety guard rail to make
sure we do not put just any program path  `/etc/shells` because shells are so important.
You may be prompted for your password.Type it and press `enter` (or `return`) to proceed.

Next, add the line that you copied to the very end on its own line of the file.
For example, if your `/etc/shells` file initially looks like this:

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

Then, after adding `/opt/homebrew/bin/bash`, it should look like this:

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
/opt/homebrew/bin/bash
```

Save the file and close it. Finally, run the *change shell* command with the
path you copied earlier:

```bash
chsh -s /opt/homebrew/bin/bash
```

You may be prompted for your password again, so be sure to enter it. For
good measure, restart your terminal (close it and open it again)

To verify, success, run:

```bash
echo $SHELL
```

You should see:

```text
/opt/homebrew/bin/bash
```

## Reconfigure Homebrew on your Shell (Apple Silicon)

Recall earlier that the Homebrew installation modified by your `PATH` variable via
a file called `~/.zprofile`. Since that file is specific to the Z shell (`zsh`),
and we are using `bash`, we may need modify the corresponding `bash`-specific file
to with the `PATH` variable.

To see if this is necessary, run the `brew doctor` command:

```bash
brew doctor
```

If it cannot find `brew`,  then you may need to do some other steps:

- Open your `.bash_profile` file in your home directory with the `open` command:

```bash
open $HOME/.bash_profile
```

- Add the following on its own line at the very end:

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

- Save the file and close it.

- Reopen your terminal (close and open it again), and type:

```bash
brew doctor
```

You should see:

```text
Your system is ready to brew
```

## References

- [Video walkthrough on making `bash` the default macOS shell](https://www.youtube.com/watch?v=AWQ7LNT9vME)
