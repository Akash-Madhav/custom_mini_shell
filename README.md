# Custom Mini Shell v3.0

A powerful, modular, and dynamic Python-based mini shell designed for Operating Systems practical work and terminal simulation.

## 🚀 Key Features
- **Modular Architecture**: Clean separation of concerns (Filesystem, System, Registry, UI).
- **Dynamic Prompt**: Colorful `user@hostname:path$` prompt with real-time directory updates.
- **Enhanced Built-ins**: Support for common UNIX-like commands (`ls -a`, `mkdir`, `touch`, `rm -r`, etc.).
- **Command Registry**: Easily extensible command mapping logic.
- **Session History**: Track commands run during the current session.
- **ANSI Color Support**: High-end terminal aesthetics (Blue, Green, Cyan, Red).

## 📁 Project Structure
The project is organized into modular files for maximum clarity:

- `shell.py`: Entry point and main interactive loop.
- `registry.py`: Centralized command lookup and registration.
- `filesystem.py`: Core logic for file and directory operations (`ls`, `cd`, `mkdir`, `rm`, `touch`, `cat`).
- `system.py`: General shell utilities (`clear`, `echo`, `whoami`, `help`).
- `colors.py`: Terminal color constants for a premium UI experience.
- `README.md`: Project documentation.

## 🛠️ Built-in Commands
| Command | Usage | Description |
| :--- | :--- | :--- |
| **cd** | `cd [path]` | Change directory (defaults to home). |
| **pwd** | `pwd` | Show the current working directory. |
| **ls** | `ls [-a] [path]` | List files/folders (use `-a` for hidden files). |
| **mkdir** | `mkdir <dir>` | Create one or more directories. |
| **touch** | `touch <file>` | Create empty files or update timestamps. |
| **rm** | `rm [-r] <path>` | Remove files or directories (`-r` for recursive). |
| **cat** | `cat <file>` | Display file contents in the terminal. |
| **whoami**| `whoami` | Show the current system user. |
| **echo** | `echo [text]` | Print text to the console. |
| **history**| `history` | View command history for the current session. |
| **clear** | `clear` | Clear the terminal screen. |
| **help**  | `help` | Show this command list. |
| **exit**  | `exit` | Gracefully exit the shell. |

*Any non-built-in command (e.g., `git`, `python`, `ipconfig`) is automatically passed to the system shell.*

## 🐍 Virtual Environment (VENV)
This project includes a dedicated virtual environment for better dependency management and to keep your global Python installation clean.

### Setup & Activation
To activate the environment on Windows:
```powershell
.\venv\Scripts\activate
```

To deactivate the environment:
```powershell
deactivate
```

*Note: The shell's startup sequence will automatically report if the VENV is active or not.*


## 💻 How To Run
1. Ensure you have Python 3.x installed.
2. Open your terminal in this directory.
3. Activate the VENV (see above).
4. Run:
   ```bash
   python shell.py
   ```

## 🎓 OS Concepts Demonstrated
- **Modular Design**: Demonstrates how OS components (like shells) are structured into subsystems.
- **Process Management**: Uses `subprocess` to spawn and manage external system processes.
- **Filesystem Interface**: Interacts with the OS kernel through `os` and `shutil` APIs.
- **User Environment**: Retrieves system metadata like hostname, username, and environment variables.
- **Error Handling**: Implements defensive programming to handle invalid inputs and OS exceptions.
- **Isolated Environments**: Demonstrates the use of virtual environments (VENV) to maintain system integrity.


---
