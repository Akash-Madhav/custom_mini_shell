import os
import getpass
from colors import GREEN, YELLOW, CYAN, RESET, BOLD

def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def echo_command(args):
    """Print the arguments to the shell."""
    print(" ".join(args[1:]))


def whoami_command():
    """Print the current user."""
    print(getpass.getuser())


def print_help():
    """Display supported commands and examples."""
    print(f"{YELLOW}{BOLD}Custom Mini Shell - Available Commands:{RESET}")
    
    # Standard Commands
    std_cmds = [
        ("cd [path]", "Change directory (default: home)"),
        ("pwd", "Show current directory"),
        ("ls [-a] [path]", "List files/folders (-a for hidden)"),
        ("echo [text]", "Print text to terminal"),
        ("whoami", "Show current user"),
        ("clear", "Clear terminal screen"),
        ("exit", "Exit mini shell")
    ]
    
    # Filesystem Commands
    fs_cmds = [
        ("mkdir <dir>", "Create one or more directories"),
        ("touch <file>", "Create empty files"),
        ("rm [-r] <path>", "Remove files or directories"),
        ("cat <file>", "Display file contents"),
    ]

    # Unique/Custom Commands
    extra_cmds = [
        ("sysinfo", "Show unique system summary"),
        ("calc <expr>", "Evaluate math (e.g., calc 10*5)"),
        ("search <term>", "Search text inside all local files"),
        ("notes <add/clear>", "Manage persistent shell notes"),
    ]

    print(f"\n{CYAN}[ Standard ]{RESET}")
    for cmd, desc in std_cmds:
        print(f"  {GREEN}{cmd:<15}{RESET} {desc}")
        
    print(f"\n{CYAN}[ Filesystem ]{RESET}")
    for cmd, desc in fs_cmds:
        print(f"  {GREEN}{cmd:<15}{RESET} {desc}")

    print(f"\n{CYAN}[ Unique / Custom ]{RESET}")
    for cmd, desc in extra_cmds:
        print(f"  {GREEN}{cmd:<15}{RESET} {desc}")
    
    print(f"\n{YELLOW}System commands are also supported (e.g., git, python).{RESET}")

