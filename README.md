# password-toolkit

All in one password tool app so that the user can check their password strength (most are weak) and evaluate
if password is weak or not, how to strengthen it, encode passwords and also allow generating passwords automatically.

## Authors
hub07777
## Description
A terminal app that displays a menu with seperate options such as
1: user can input a password and the app will check how strong it is from 0-5 and add suggestions to the user based on what's missing for a secure password.
4: User can input a password which will then be checked using the haveibeenpwned API, if it has been leaked previously it will display a warning message to change it and by how many times it has appeared in data breaches
5: View the log. Every strength check and breach check is saved to log.txt with a timestamp, so you can look back at past results later. The passwords themselves are never saved, only the results (for example, [2026-11-20 05:58] Strength check: 4/5 (Strong)).
## Purpose
## How to run
pip install -r requirements.txt
## Features
## Points to be graded
## Todo
Cipher ig maybe I dont do it ngl