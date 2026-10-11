
import os
import getpass
import subprocess
import random
import platform
import time
import ast
import operator
from datetime import datetime

print("===== Shortcut Terminal =====")
print("Type 'help' for a list of commands.")

def calculate(expression):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise ValueError("Exponent is too large.")

            return operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -evaluate(node.operand)
            if isinstance(node.op, ast.UAdd):
                return evaluate(node.operand)

        raise ValueError("Invalid math expression.")

    return evaluate(ast.parse(expression, mode="eval").body)


while True:
    try:
        command = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nShortcut Terminal closed.")
        break

    if not command:
        continue

    elif command == "help":
        print("""
===== Shortcut Terminal Commands =====

help                  - List all commands
openApp [app name]    - Open an application
userName              - Show your Windows username
timeIs                - Show the current local time
dateIs                - Show the current local date
calc [math]           - Calculate a math expression
listFiles             - List files in the current folder
whereAmI              - Show the current directory
timer [seconds]       - Start a countdown timer
readFile [filename]   - Read a text file
rollDice              - Roll a six-sided die
systemInfo            - Show basic system information
say [message]         - Print a message
clear                 - Clear the terminal screen
exit                  - Close Shortcut Terminal
""")

    elif command == "userName":
        print("Windows username:", getpass.getuser())

    elif command == "timeIs":
        print("Current time:",
              datetime.now().astimezone().strftime("%I:%M:%S %p"))

    elif command == "dateIs":
        print("Current date:",
              datetime.now().astimezone().strftime("%B %d, %Y"))

    elif command.startswith("openApp "):
        app_name = command[len("openApp "):].strip()

        if app_name:
            try:
                subprocess.Popen(
                    ["cmd", "/c", "start", "", app_name],
                    shell=False
                )
                print("Opening:", app_name)
            except OSError as error:
                print("Could not open application:", error)
        else:
            print("Usage: openApp [app name]")

    elif command.startswith("calc "):
        expression = command[len("calc "):].strip()

        try:
            print("Result:", calculate(expression))
        except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
            print("Invalid calculation. Example: calc 25 + 15")

    elif command == "listFiles":
        try:
            for item in sorted(os.listdir()):
                if os.path.isdir(item):
                    print("[Folder]", item)
                else:
                    print("[File]", item)
        except OSError as error:
            print("Could not list files:", error)

    elif command == "whereAmI":
        print("Current directory:", os.getcwd())

    elif command.startswith("timer "):
        value = command[len("timer "):].strip()

        try:
            seconds = int(value)

            if seconds < 0 or seconds > 86400:
                print("Enter a number from 0 to 86400 seconds.")
            else:
                print("Timer started for", seconds, "seconds.")
                time.sleep(seconds)
                print("Timer finished!")
        except ValueError:
            print("Usage: timer [whole number of seconds]")

    elif command.startswith("readFile "):
        filename = command[len("readFile "):].strip()

        try:
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found:", filename)
        except (OSError, UnicodeError) as error:
            print("Could not read file:", error)

    elif command == "rollDice":
        print("You rolled a", random.randint(1, 6), "!")

    elif command == "systemInfo":
        print("===== System Information =====")
        print("Operating system:", platform.system())
        print("OS version:", platform.version())
        print("Computer name:", platform.node())
        print("Architecture:", platform.machine())
        print("Python version:", platform.python_version())

    elif command.startswith("say "):
        message = command[len("say "):]
        print(message)

    elif command == "clear":
        os.system("cls" if os.name == "nt" else "clear")

    elif command == "exit":
        print("Closing terminal...")
        break

    else:
        print("Unknown command. Type 'help' to see available commands.")
