import os
import platform
import datetime
from colors import GREEN, BLUE, YELLOW, RED, RESET, BOLD, CYAN

def sysinfo_command():
    """Display unique system information with premium formatting."""
    print(f"{YELLOW}{BOLD}--- SYSTEM SUMMARY ---{RESET}")
    print(f"{CYAN}OS:{RESET}        {platform.system()} {platform.release()}")
    print(f"{CYAN}Node:{RESET}      {platform.node()}")
    print(f"{CYAN}Processor:{RESET} {platform.processor()}")
    print(f"{CYAN}Python:{RESET}    {platform.python_version()}")
    print(f"{CYAN}Time:{RESET}      {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{YELLOW}{BOLD}----------------------{RESET}")


def calc_command(args):
    """Simple built-in calculator."""
    if len(args) < 2:
        print(f"{RED}calc: missing expression (e.g., calc 2+2){RESET}")
        return
    
    expr = "".join(args[1:])
    try:
        # Using a restricted eval for safety
        allowed_chars = "0123456789+-*/(). "
        if all(c in allowed_chars for c in expr):
            result = eval(expr)
            print(f"{GREEN}Result:{RESET} {result}")
        else:
            print(f"{RED}calc: invalid characters in expression{RESET}")
    except Exception as exc:
        print(f"{RED}calc error: {exc}{RESET}")


def search_command(args):
    """Search for a string in all text files in the current directory."""
    if len(args) < 2:
        print(f"{RED}search: missing search term{RESET}")
        return
    
    term = args[1].lower()
    print(f"{BLUE}Searching for '{term}' (case-insensitive)...{RESET}")
    
    found = False
    for filename in os.listdir("."):
        if os.path.isfile(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        if term in line.lower():
                            print(f"{GREEN}{filename}:{i}:{RESET} {line.strip()}")
                            found = True

            except:
                continue # Skip binary files or encoding errors
    
    if not found:
        print(f"{YELLOW}No matches found.{RESET}")


def notes_command(args):
    """Simple persistent note-taker."""
    notes_file = ".shell_notes.txt"
    
    if len(args) < 2:
        # List notes
        if not os.path.exists(notes_file):
            print(f"{YELLOW}No notes found.{RESET}")
        else:
            print(f"{CYAN}{BOLD}--- YOUR NOTES ---{RESET}")
            with open(notes_file, 'r') as f:
                print(f.read().strip())
            print(f"{CYAN}{BOLD}------------------{RESET}")
        return

    subcmd = args[1].lower()
    if subcmd == "add":
        note = " ".join(args[2:])
        if not note:
            print(f"{RED}notes add: missing text{RESET}")
            return
        with open(notes_file, 'a') as f:
            f.write(f"- {note} ({datetime.datetime.now().strftime('%H:%M')})\n")
        print(f"{GREEN}Note added!{RESET}")
    elif subcmd == "clear":
        if os.path.exists(notes_file):
            os.remove(notes_file)
            print(f"{GREEN}Notes cleared.{RESET}")
    else:
        print(f"{RED}Unknown notes command. Use 'add' or 'clear'.{RESET}")
