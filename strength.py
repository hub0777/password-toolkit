from file_manager import save_to_log as sl

def check_password_strength(password):      
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    missing = []
    strength = {5: "Very Strong", 4: "Strong", 3: "Moderate", 2: "Weak", 1: "Very Weak", 0: "Extremely Weak"}

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum(): 
            has_symbol = True
  
    checks = [
        (has_lower, "Add a lowercase letter"),
        (has_upper, "Add an uppercase letter"),
        (has_digit, "Add a digit"),
        (has_symbol, "Add a symbol")
    ]

    for check, message in checks:
        if check == False:
            missing.append(message)


    if len(password) < 8:
        missing.append("Tip: Make password 8 or more characters")
         

    score = 5 - len(missing)
    sl(f"Strength check: {score}/5 ({strength[score]})")
    print(f"Score: {score}/5")
    print(f"Strength Level: {strength[score]}")
    for i in missing:
        print(i)

    if len(missing) == 0:
        print("Your password is strong!")

