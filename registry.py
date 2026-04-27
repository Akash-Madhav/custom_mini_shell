from filesystem import (
    change_directory,
    print_working_directory,
    list_files,
    mkdir_command,
    touch_command,
    rm_command,
    cat_command
)
from system import (
    clear_screen,
    echo_command,
    whoami_command,
    print_help
)
from extra_commands import (
    sysinfo_command,
    calc_command,
    search_command,
    notes_command
)

# Command Registry mapping command strings to functions
COMMAND_MAP = {
    "cd": change_directory,
    "pwd": print_working_directory,
    "ls": list_files,
    "clear": clear_screen,
    "help": print_help,
    "echo": echo_command,
    "mkdir": mkdir_command,
    "touch": touch_command,
    "rm": rm_command,
    "cat": cat_command,
    "whoami": whoami_command,
    "sysinfo": sysinfo_command,
    "calc": calc_command,
    "search": search_command,
    "notes": notes_command,
}

def get_command(cmd_name):
    """Retrieve command function from the registry."""
    return COMMAND_MAP.get(cmd_name.lower())
