import display
from strength import check_password_strength as cs
from breach import check_breach as cb
from file_manager import save_to_log as sl, view_log as vl
from generator import generate_password as gp
from cipher import CaesarCipher
from validators import is_whole_number


def handle_cipher():
    """Ask the user to encode or decode, then run the Caesar cipher."""
    mode = input("Type 'e' to encode or 'd' to decode: ").strip().lower()
    try:
        if mode != "e" and mode != "d":
            raise ValueError("Choose 'e' or 'd'.")
        text = input("Enter the text: ")
        if text == "":
            raise ValueError("Text cannot be empty.")
        shift_text = input("Enter a shift between 1 and 25: ")
        if not is_whole_number(shift_text):
            raise ValueError("Please type a whole number, like 3.")
        shift = int(shift_text)
        if shift < 1 or shift > 25:
            raise ValueError("Shift must be between 1 and 25.")

        cipher = CaesarCipher(shift)
        if mode == "e":
            result = cipher.encode(text)
            sl("Encoded a message with " + cipher.describe())
        else:
            result = cipher.decode(text)
            sl("Decoded a message with " + cipher.describe())
        display.print_success("Result: " + result)
    except ValueError as e:
        display.print_error(f"Invalid input: {e}")


def run_menu():
    """Run the menu loop until the user types exit."""
    display.show_banner()
    while True:
        display.show_menu()
        choice = input("Choose a number option such as 1: ").strip().lower()

        if choice == "exit":
            display.print_info("Goodbye!")
            break
        elif choice == "1":
            password = input("Enter a password to check its strength: ")
            try:
                if password == "":
                    raise ValueError("Password cannot be empty.")  # thanks w3schools
                cs(password)
            except ValueError as e:
                display.print_error(f"Invalid input: {e}")
        elif choice == "2":
            try:
                length_text = input("Enter a password length to generate: ")
                if not is_whole_number(length_text):
                    raise ValueError("Please type a whole number, like 12.")
                length = int(length_text)
                if length < 8 or length > 64:
                    raise ValueError("Length must be between 8 and 64.")
                gp(length)
                sl(f"Generated a password of {length} characters")
            except ValueError as e:
                display.print_error(f"Invalid length: {e}")
        elif choice == "3":
            handle_cipher()
        elif choice == "4":
            password = input("Enter a password to check for breaches: ")
            try:
                if password == "":
                    raise ValueError("Password cannot be empty.")
                cb(password)
            except ValueError as e:
                display.print_error(f"Invalid input: {e}")
        elif choice == "5":
            sl("User viewed the log.")
            vl()
        else:
            display.print_error("Invalid option, try again.")