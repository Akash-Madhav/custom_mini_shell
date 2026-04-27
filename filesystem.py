import os
import shutil
from colors import BLUE, GREEN, RED, CYAN, RESET, BOLD

def change_directory(args):
    """Change current working directory."""
    if len(args) < 2:
        target = os.path.expanduser("~")
    else:
        target = args[1]
    
    try:
        os.chdir(target)
    except Exception as exc:
        print(f"{RED}cd: {exc}{RESET}")


def print_working_directory():
    """Print current working directory."""
    print(f"{CYAN}{os.getcwd()}{RESET}")


def list_files(args):
    """List files in current directory or optional target directory."""
    show_all = "-a" in args
    target = os.getcwd()
    
    paths = [a for a in args[1:] if not a.startswith("-")]
    if paths:
        target = paths[0]

    try:
        items = os.listdir(target)
        if not show_all:
            items = [i for i in items if not i.startswith(".")]
        
        items.sort()
        
        for name in items:
            full_path = os.path.join(target, name)
            if os.path.isdir(full_path):
                print(f"{BLUE}{BOLD}{name}/{RESET}")
            elif os.access(full_path, os.X_OK):
                print(f"{GREEN}{name}*{RESET}")
            else:
                print(name)
    except Exception as exc:
        print(f"{RED}ls: {exc}{RESET}")


def mkdir_command(args):
    """Create a new directory."""
    if len(args) < 2:
        print(f"{RED}mkdir: missing operand{RESET}")
        return
    
    for folder in args[1:]:
        try:
            os.makedirs(folder, exist_ok=True)
        except Exception as exc:
            print(f"{RED}mkdir: cannot create directory '{folder}': {exc}{RESET}")


def touch_command(args):
    """Create an empty file or update timestamp."""
    if len(args) < 2:
        print(f"{RED}touch: missing file operand{RESET}")
        return
    
    for filename in args[1:]:
        try:
            with open(filename, 'a'):
                os.utime(filename, None)
        except Exception as exc:
            print(f"{RED}touch: cannot touch '{filename}': {exc}{RESET}")


def rm_command(args):
    """Remove files or directories."""
    if len(args) < 2:
        print(f"{RED}rm: missing operand{RESET}")
        return
    
    recursive = "-r" in args
    targets = [a for a in args[1:] if not a.startswith("-")]
    
    for target in targets:
        try:
            if os.path.isdir(target):
                if recursive:
                    shutil.rmtree(target)
                else:
                    print(f"{RED}rm: cannot remove '{target}': Is a directory (use -r){RESET}")
            else:
                os.remove(target)
        except Exception as exc:
            print(f"{RED}rm: cannot remove '{target}': {exc}{RESET}")


def cat_command(args):
    """Display file contents."""
    if len(args) < 2:
        print(f"{RED}cat: missing file operand{RESET}")
        return
    
    for filename in args[1:]:
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except Exception as exc:
            print(f"{RED}cat: {filename}: {exc}{RESET}")
