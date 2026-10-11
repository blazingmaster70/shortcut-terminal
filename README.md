# Shortcut Terminal

**A simple command-line utility built with Python.**

Shortcut Terminal is a beginner-friendly Python program that lets you run useful commands directly from a single terminal interface. It includes tools for calculations, file management, timers, system information, and opening applications on Windows.

## Features

- **Application Launcher** — Open applications using `openApp`.
- **Username** — Display your Windows username.
- **Current Time** — Display the current local time.
- **Current Date** — Display the current local date.
- **Calculator** — Perform arithmetic calculations.
- **File Listing** — View files and folders in the current directory.
- **Directory Information** — Display the current working directory.
- **Countdown Timer** — Wait for a specified number of seconds.
- **Text File Reader** — Read the contents of text files.
- **Dice Roller** — Generate a random number from 1 to 6.
- **System Information** — Display operating system, computer name, architecture, and Python version.
- **Message Printer** — Print custom messages.
- **Screen Clearing** — Clear the terminal screen.
- **Help System** — Display the available commands.
- **Exit Command** — Close Shortcut Terminal.

## Requirements

- Python 3
- Windows recommended for application-launching functionality
- No additional Python packages required

## Installation

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Save the program as `shortcut_terminal.py`.
3. Open Command Prompt or a terminal.
4. Navigate to the folder containing the file.
5. Run the program:

```bash
python shortcut_terminal.py
```

## Commands

| Command | Description | Example |
|---|---|---|
| `help` | Display available commands | `help` |
| `openApp [app name]` | Open an application | `openApp notepad` |
| `userName` | Display your Windows username | `userName` |
| `timeIs` | Display the current local time | `timeIs` |
| `dateIs` | Display the current local date | `dateIs` |
| `calc [math]` | Calculate a mathematical expression | `calc 25 + 15` |
| `listFiles` | List files and folders | `listFiles` |
| `whereAmI` | Display the current directory | `whereAmI` |
| `timer [seconds]` | Start a countdown timer | `timer 10` |
| `readFile [filename]` | Display a text file | `readFile notes.txt` |
| `rollDice` | Roll a six-sided die | `rollDice` |
| `systemInfo` | Display basic system information | `systemInfo` |
| `say [message]` | Print a message | `say Hello!` |
| `clear` | Clear the terminal screen | `clear` |
| `exit` | Close the program | `exit` |

## Example Session

```text
===== Shortcut Terminal =====
Type 'help' for a list of commands.

> calc 25 + 15
Result: 40

> say Welcome to Shortcut Terminal!
Welcome to Shortcut Terminal!

> rollDice
You rolled a 4 !

> whereAmI
Current directory: C:\Users\YourName

> exit
Shortcut Terminal closed.
```

*Example output is illustrative; actual results will vary.*

## How It Works

Shortcut Terminal uses Python's built-in modules to provide its functionality:

- `os` — Directory listing and screen clearing.
- `getpass` — Retrieve the current Windows username.
- `subprocess` — Launch applications.
- `random` — Generate random dice results.
- `platform` — Retrieve system information.
- `time` — Implement countdown timers.
- `datetime` — Retrieve local date and time.
- `ast` and `operator` — Evaluate supported mathematical expressions safely.

The program uses a command loop to accept multiple commands until the user enters `exit`.

## Limitations

- The username command returns the Windows username, which may differ from the Microsoft account display name.
- The displayed date and time depend on the computer's clock and time-zone settings.
- The calculator supports basic arithmetic operations rather than a complete mathematical language.
- The timer blocks command input until the countdown finishes.
- The file reader is intended for text files.
- Application launching depends on Windows and the application's availability.

## Project Goal

Shortcut Terminal aims to make common computer tasks simple and accessible through short, memorable commands. It also serves as a practical Python project for learning command processing, functions, file handling, system utilities, and error handling.

## License

No license has been specified for this project. Add a license before redistributing the code if you want to define permissions for reuse and modification.

---

**Shortcut Terminal**  
Built with Python.
