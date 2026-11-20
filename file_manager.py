from datetime import datetime
def save_to_log(text):
    """Save the given text to a log file."""
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("log.txt", "a") as log_files: # Open the log file in append mode, so new entries are added to the end of the file
        log_files.write(f"[{time}] {text}\n")

def view_log():
    """ View the contents of the log file."""
    try:
        with open("log.txt", "r") as log_files: # Open the log file in read mode
            content = log_files.read() # Read the entire content of the log file
            print("=== Log Content ===")
            print(content) # Print the content of the log file
            if content == "":
                print("No logs to display.") # If the log file is empty
    except FileNotFoundError:
        print("Log file not found. No logs to display.") # If the log file does not exist
      