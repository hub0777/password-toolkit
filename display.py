"""Console display helpers: colours, banner, slow printing and the menu."""

import time
from colorama import Fore, Style

# Colours imported from colorama library (thanks geeks4geeks)
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL

BANNER = """
==================================
        P A S S W O R D
         T O O L K I T
==================================
"""

# Each menu option is a tuple: (what the user types, what the option does)
MENU_OPTIONS = [
    ("1", "Check password strength"),
    ("2", "Generate a secure password"),
    ("3", "Encode / decode (cipher)"),
    ("4", "Check if a password was breached"),
    ("5", "View log"),
]


def colour_text(text, colour):
    """Return the text wrapped in a colour code and a reset code."""
    return colour + text + RESET


def print_success(text):
    """Print a message in green."""
    print(colour_text(text, GREEN))


def print_warning(text):
    """Print a message in yellow."""
    print(colour_text(text, YELLOW))


def print_error(text):
    """Print a message in red."""
    print(colour_text(text, RED))


def print_info(text):
    """Print a message in cyan."""
    print(colour_text(text, CYAN))


def slow_print(text, delay=0.02):
    """Print text one character at a time, pausing `delay` seconds between each."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def show_banner():
    """Print the app banner in bold cyan, one line at a time."""
    lines = BANNER.split("\n")
    for line in lines:
        print(colour_text(line, CYAN + BOLD))
        time.sleep(0.05)


def show_menu():
    """Print the main menu with coloured option numbers."""
    print()
    print(colour_text("Main menu", BOLD))
    for number, label in MENU_OPTIONS:
        print("  " + colour_text("[" + number + "]", CYAN) + " " + label)
    print("  " + colour_text("[exit]", RED) + " Quit")
    print()


def print_score(score):
    """Print a strength score in red (0-2), yellow (3) or green (4-5)."""
    message = "Strength score: " + str(score) + "/5"
    if score <= 2:
        print_error(message)
    elif score == 3:
        print_warning(message)
    else:
        print_success(message)