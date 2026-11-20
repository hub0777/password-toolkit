# password-toolkit

All in one password tool app so that the user can check their password strength (most are weak) and evaluate
if password is weak or not, how to strengthen it, encode passwords and also allow generating passwords automatically.

## Authors
hub07777
## Description
A terminal app that displays a menu with seperate options such as
1: user can input a password and the app will check how strong it is from 0-5 and add suggestions to the user based on what's missing for a secure password.
2: Generate a password. Creates a random password between 8 and 64 characters using the secrets module, and skips confusing characters like 0/O and l/1/I.
3: Encoding (coming soon)
4: User can input a password which will then be checked using the haveibeenpwned API, if it has been leaked previously it will display a warning message to change it and by how many times it has appeared in data breaches
5: View the log. Every strength check and breach check is saved to log.txt with a timestamp, so you can look back at past results later. The passwords themselves are never saved, only the results (for example, [2026-11-20 05:58] Strength check: 4/5 (Strong)).
## Purpose
Passswod stuff 
## How to run
pip install -r requirements.txt
## Points to be graded
- Menu that returns after each option and only exits on "exit"
- Functions split across separate files, main.py only calls run_menu()
- Imports use "as" aliases
- Dictionary (strength ratings), list of tuples (strength checks), set (skipped characters), lists
- Exception handling: raise ValueError for invalid input, RequestException for API errors, FileNotFoundError for the log
- Data validation: empty passwords and lengths outside 8-64 are rejected
- Uses an API (Have I Been Pwned, only first 5 hash characters sent)
- External file: log.txt with timestamps, separate save and view functions
- Docstrings on all functions
- Atomic Git commits
- README.md and requirements.txt
## Features
In description
## Todo
Cipher.py (I guess cipher.py)