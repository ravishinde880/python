import string


def check_password(password):
    suggestions = []

    # Check length
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Check lowercase
    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Check number
    if not any(char.isdigit() for char in password):
        suggestions.append("Add at least one number (0-9).")

    # Check special character
    if not any(char in string.punctuation for char in password):
        suggestions.append(
            "Add at least one special character (!, @, #, $, etc.)."
        )

    # Calculate strength
    checks_passed = 5 - len(suggestions)

    if len(password) >= 12 and checks_passed == 5:
        strength = "VERY STRONG"
    elif len(password) >= 8 and checks_passed >= 4:
        strength = "STRONG"
    elif checks_passed >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return strength, suggestions


# Main program
print("=" * 50)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 50)

password = input("Enter your password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

print("\nSecurity Checks:")
print(
    "Length:",
    "PASS" if len(password) >= 8 else "FAIL"
)
print(
    "Uppercase:",
    "PASS" if any(c.isupper() for c in password) else "FAIL"
)
print(
    "Lowercase:",
    "PASS" if any(c.islower() for c in password) else "FAIL"
)
print(
    "Number:",
    "PASS" if any(c.isdigit() for c in password) else "FAIL"
)
print(
    "Special Character:",
    "PASS" if any(c in string.punctuation for c in password) else "FAIL"
)

if suggestions:
    print("\nHow to improve your password:")

    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nExcellent! Your password meets all requirements.")