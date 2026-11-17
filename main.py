from utils import show_menu


def main():
    """Run the menu loop until the user types exit."""
    while True:
        show_menu()
        choice = input("Choose a number option such as 1: ").strip().lower()

        if choice == "exit":
            print("Goodbye!")
            break
        elif choice == "1":
            print("Strength checker coming soon")
        elif choice == "2":
            print("Generator coming soon")
        elif choice == "3":
            print("Encoder coming soon")
        elif choice == "4":
            print("Breach checker coming soon")
        elif choice == "5":
            print("Log viewer coming soon")
        else:
            print("Invalid option, try again.")


if __name__ == "__main__": # thanks
    main()