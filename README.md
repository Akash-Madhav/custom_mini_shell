# Custom Mini Shell

A simple Python-based mini shell for Operating Systems practical work.

## Objective

Build a terminal-like program that:
- accepts user commands,
- executes built-in shell commands,
- executes system commands,
- and maintains current working directory state.

## Project Files

- `shell.py`: Main loop, command parsing, and external command execution.
- `commands.py`: Built-in command implementations.
- `README.md`: Documentation and viva explanation points.

## Built-in Commands

- `cd <path>`: Change current directory.
- `pwd`: Print current directory.
- `ls [path]`: List files/folders.
- `clear`: Clear terminal screen.
- `help`: Show command usage.
- `exit`: Exit the shell.

Any non-built-in command is executed through the OS (examples: `echo hello`, `dir`, `mkdir test`).

## How To Run

1. Open terminal in this folder.
2. Run:

```bash
python shell.py
```

## Demo Script (for viva)

Run these commands in order:

```text
pwd
ls
cd ..
pwd
cd invalid_folder
help
echo hello
exit
```

Expected behavior:
- Directory changes persist across commands.
- Invalid paths show clean error messages.
- External commands run normally.
- Shell exits only when `exit` is entered.

## OS Concepts Demonstrated

- **Shell as user-OS interface**: takes user input and sends actions to OS.
- **Filesystem navigation**: `cd`, `pwd`, `ls` use Python `os` APIs.
- **Process execution**: external commands run using `subprocess.run`.
- **Error handling**: robust handling for invalid paths and command errors.

## Limitations (intentional for simplicity)

- Basic token parsing (`split`) is used.
- Complex quoting, pipes, and redirection are not implemented.
- Designed mainly for Windows demo environment.
