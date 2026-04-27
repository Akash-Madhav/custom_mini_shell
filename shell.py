import os
import subprocess
import socket
import getpass
import inspect
import sys

from colors import GREEN, BLUE, YELLOW, RED, CYAN, RESET, BOLD
from registry import get_command
from system import clear_screen

# History tracking
command_history = []

def run_system_command(command_str):
    """Run non-built-in command using the system shell."""
    try:
        completed = subprocess.run(command_str, shell=True)
    except Exception as exc:
        print(f"{RED}Error while executing command: {exc}{RESET}")


def handle_command(command_str):
    """Route command to built-ins or external execution."""
    parts = command_str.split()
    if not parts:
        return

    cmd_name = parts[0]
    func = get_command(cmd_name)

    if func:
        # Check if function takes args
        sig = inspect.signature(func)
        if len(sig.parameters) > 0:
            func(parts)
        else:
            func()
    elif cmd_name.lower() == "history":
        for i, h in enumerate(command_history, 1):
            print(f"  {i}  {h}")
    else:
        run_system_command(command_str)


def get_prompt():
    """Construct a dynamic, colorful prompt."""
    user = getpass.getuser()
    hostname = socket.gethostname()
    cwd = os.getcwd()
    
    home = os.path.expanduser("~")
    if cwd.startswith(home):
        cwd = cwd.replace(home, "~", 1)
    
    return f"{GREEN}{user}@{hostname}{RESET}:{BLUE}{cwd}{RESET}$ "


def initialize_shell():
    """Perform startup checks and initialize environment."""
    print(f"{CYAN}Initializing System...{RESET}")
    
    # Check for core modules
    modules = ["filesystem.py", "system.py", "registry.py", "extra_commands.py", "colors.py"]
    missing = [m for m in modules if not os.path.exists(m)]
    
    if missing:
        print(f"{RED}Warning: Missing core modules: {', '.join(missing)}{RESET}")
    else:
        print(f"{GREEN}Core Modules: OK{RESET}")

    # Check for VENV
    if hasattr(sys, 'real_prefix') or (target := getattr(sys, 'base_prefix', sys.prefix)) != sys.prefix:
        print(f"{GREEN}Environment: Virtual (VENV active){RESET}")
    else:
        print(f"{YELLOW}Environment: Global (VENV not active){RESET}")
    
    # Load history or other state if needed
    print(f"{GREEN}System Check Complete.{RESET}\n")


def run_shell():
    """Main interactive shell loop."""
    clear_screen()
    print(f"{YELLOW}{BOLD}Welcome to Custom Mini Shell v3.1{RESET}")
    print(f"Type {GREEN}'help'{RESET} to see available commands or {RED}'exit'{RESET} to quit.\n")
    
    initialize_shell()

    while True:
        try:
            command = input(get_prompt()).strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{YELLOW}Exiting shell...{RESET}")
            break

        if not command:
            continue

        if command.lower() == "exit":
            print(f"{YELLOW}Goodbye!{RESET}")
            break

        command_history.append(command)
        handle_command(command)


if __name__ == "__main__":
    # Enable colors on Windows
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    
    run_shell()
