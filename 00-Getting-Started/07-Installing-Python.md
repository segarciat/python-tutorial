# 7. Installing Python with Rye

On macOS, Python comes pre-installed. You can verify by running either of the following
commands, which displays its version:

```bash
type -P python
python --version
```

Our goal in this section is to install an up-to-date Python version. We could achieve
this by [installing Python from the official website](https://www.python.org/downloads/macos/).
Unfortunately, this is not necessarily ideal. Instead, we will install Python
through a newly available command-line tool called Rye.

## What is Rye?

[**Rye**](https://rye.astral.sh/) is a command-line program that provides a unified,
all-in-one experience for managing our Python projects.

We get the following:

- **Easily install different Python versions**: Sometimes you need to work with more than one Python
version, or you wish to upgrade to the latest one. We can do that with Rye easily.

- **Isolate project environments**: Python projects often use libraries or packages. For example, many mathematical and scientific programs use a library called [**numpy**](https://numpy.org/doc/stable/user/whatisnumpy.html). If two projects used the same version of `numpy`, and we accidentally updated it for one project, then it might break the other project because the versions may not be compatible! Separate environments eliminate this issue.

- **Formatting**: Rye provides a code formatter. Proper formatting and styling ensures our code is neat. This is important, because if we go back to the code a week later, the formatting should make it easy to follow the flow of the program. Just as important, others may view our code, and a consistent format makes it easier for them to understand.

There are other features, such as testing, linting, and much more.

## Installing Rye

Your system likely does not have the `rye` command; you can verify it by running:

```bash
rye --version
```

[Installing Rye is easy](https://rye.astral.sh/). Copy the following command,
paste it into your terminal, and run it:

```bash
curl -sSf https://rye.astral.sh/get | bash
```

This command pipeline will download a script that will be interpreted by `bash`
to install `rye`.

You will see messages guiding you through the installation. Use the arrow keys in
your keyboard, and `enter` when approrpiate. If you get stuck, see the article
[Install Python with Rye on mac.install.guide](https://mac.install.guide/python/install-rye).

Here's a brief summary:

1. Press `y` to continue.
2. Select `pip-tools` for comptability (even though it's "slower").
3. Opt to run the Python installed and managed by Rye. This way, when you type `python` or `python3`, you are interacting with the one installed by Rye, *not* your system default one.
4. Accept the suggested Python version for the default toolchain by press ENTER. At the time of writing, 3.12 is the latest version.
5. Press `y` when asked to add Rye to `PATH`.

By modifying your `PATH` variable, the Rye installation is ensuring that your
shell will recognize the `rye` command when you type it.

## Adding `rye` to your `PATH`

Assuming you are running your `bash` shell and you pressed `y` during the Rye
installation when prompted to modify your `.bash_profile` file, `rye` should already
be in your `PATH`.

However, if not, you can simply run:

```bash
echo 'source "$HOME/.rye/env"' >> ~/.bash_profile
source ~/.bash_profile
```

To ensure it worked, run:

```bash
echo $PATH
```

and observe `/Users/username/.rye/shims` at the start of your `PATH`.

Verify now that Python is installed by running the following:

```bash
python --version
```

At this point, you can run `python` and see a message such as:

```text
Python 3.12.4 (main, Jul 25 2024, 22:42:01) [Clang 18.1.8 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the "Python prompt", and it just waits for you to enter text, just like your shell, to run a command on your behalf. To exit, simply type the following and press ENTER:

```text
>>> exit()
```

You will be returned to your bash shell. You can tell it's different because
the shell prompt usually has a `%` or a `$`.

## References

- [Rye](https://rye.astral.sh/)
- [Installing Python with Rye](https://mac.install.guide/python/install-rye)
