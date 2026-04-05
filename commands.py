import os


def change_directory(args):
    """Change current working directory."""
    if len(args) < 2:
        print("cd: missing argument")
        return

    target = args[1]
    try:
        os.chdir(target)
    except FileNotFoundError:
        print(f"cd: directory not found: {target}")
    except NotADirectoryError:
        print(f"cd: not a directory: {target}")
    except PermissionError:
        print(f"cd: permission denied: {target}")
    except OSError as exc:
        print(f"cd: {exc}")


def print_working_directory():
    """Print current working directory."""
    print(os.getcwd())


def list_files(args):
    """List files in current directory or optional target directory."""
    target = args[1] if len(args) > 1 else os.getcwd()
    try:
        for name in os.listdir(target):
            print(name)
    except FileNotFoundError:
        print(f"ls: path not found: {target}")
    except NotADirectoryError:
        print(f"ls: not a directory: {target}")
    except PermissionError:
        print(f"ls: permission denied: {target}")
    except OSError as exc:
        print(f"ls: {exc}")


def clear_screen():
    """Clear terminal screen (Windows)."""
    os.system("cls" if os.name == "nt" else "clear")


def print_help():
    """Display supported commands and examples."""
    print("Built-in commands:")
    print("  cd <path>      Change directory")
    print("  pwd            Show current directory")
    print("  ls [path]      List files/folders")
    print("  clear          Clear terminal screen")
    print("  help           Show this help")
    print("  exit           Exit mini shell")
    print()
    print("Any other command is executed as a system command.")
    print("Examples: echo hello, dir, mkdir test")
