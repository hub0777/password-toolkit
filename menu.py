from utils import show_menu as sm
from strength import check_password_strength as cs
from breach import check_breach as cb

def run_menu():
    """Run the menu loop until the user types exit."""
    while True:
        sm()
        choice = input("Choose a number option such as 1: ").strip().lower()

        if choice == "exit":
            print("Goodbye!")
            break
        elif choice == "1":
            password = input("Enter a password to check its strength: ")
            try:  
                if password == "":
                    raise ValueError("Password cannot be empty.")  # thanks w3schools
                cs(password)
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == "2":
            print("Generator coming soon")
        elif choice == "3":
            print("Encoder coming soon")
        elif choice == "4":
            password = input("Enter a password to check for breaches: ")
            try:
                if password == "":
                    raise ValueError("Password cannot be empty.")
                cb(password)
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == "5":
            print("Log viewer coming soon")
        else:
            print("Invalid option, try again.")

