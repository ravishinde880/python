import string

def check_password(password):
    suggestions = []
    
    # Check length
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    
    # Check uppercase
    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")
    
    # Check lowercase
    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter.")
    
    # Check numbers
    if not any(char.isdigit() for char in password):
        suggestions.append("Add at least one number.")
    
    # Check special characters
    if not any(char in string.punctuation for char in password):
        suggestions.append("Add at least one special character.")

    if not suggestions:
        print("\nPassword Strength: STRONG")
        print("Your password meets all the basic security requirements.")
    else:
        print("\nPassword Strength: WEAK")
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print("- " + suggestion)


print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")

check_password(password)