import os
import subprocess

from commands import (
    change_directory,
    clear_screen,
    list_files,
    print_help,
    print_working_directory,
)


def run_system_command(command):
    """Run non-built-in command using the system shell."""
    try:
        completed = subprocess.run(command, shell=True)
        if completed.returncode != 0:
            print(f"Command failed with exit code {completed.returncode}")
    except Exception as exc:
        print(f"Error while executing command: {exc}")


def handle_command(command):
    """Route command to built-ins or external execution."""
    parts = command.split()
    if not parts:
        return

    cmd = parts[0].lower()

    if cmd == "cd":
        change_directory(parts)
    elif cmd == "pwd":
        print_working_directory()
    elif cmd == "ls":
        list_files(parts)
    elif cmd == "clear":
        clear_screen()
    elif cmd == "help":
        print_help()
    else:
        run_system_command(command)


def run_shell():
    """Main interactive shell loop."""
    while True:
        cwd = os.getcwd()
        try:
            command = input(f"{cwd} > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting shell...")
            break

        if command == "":
            continue

        if command.lower() == "exit":
            print("Exiting shell...")
            break

        handle_command(command)


if __name__ == "__main__":
    run_shell()
