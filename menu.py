import display 
from strength import check_password_strength as cs
from breach import check_breach as cb
from file_manager import save_to_log as sl, view_log as vl
from generator import generate_password as gp

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
                length = int(input("Enter a password length to generate: "))
                if length < 8 or length > 64:
                    raise ValueError("Length must be between 8 and 64.")
                gp(length)
                sl(f"Generated a password of {length} characters")
            except ValueError as e:
                display.print_error(f"Invalid length: {e}")
            
        elif choice == "3":
            display.print_warning("Encoder coming soon")
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

