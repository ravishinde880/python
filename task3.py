import re


# Suspicious words commonly found in phishing emails
URGENT_WORDS = [
    "urgent",
    "immediately",
    "act now",
    "account suspended",
    "account blocked",
    "verify now",
    "confirm now",
    "limited time",
    "click now",
    "security alert",
    "password expired",
    "winner",
    "congratulations",
    "payment required"
]


def analyze_email(sender, subject, body, link):
    warnings = []
    score = 0

    email_text = (subject + " " + body).lower()

    # Check sender
    if "@" not in sender:
        warnings.append("Sender address does not appear to be valid.")
        score += 2

    # Check suspicious words
    found_words = []

    for word in URGENT_WORDS:
        if word in email_text:
            found_words.append(word)

    if found_words:
        warnings.append(
            "Urgent or suspicious language found: "
            + ", ".join(found_words)
        )
        score += 2

    # Check links
    if link:
        if link.startswith("http://"):
            warnings.append("The link uses HTTP instead of HTTPS.")
            score += 2

        # Look for IP address in URL
        ip_pattern = r"https?://\d{1,3}(?:\.\d{1,3}){3}"

        if re.search(ip_pattern, link):
            warnings.append("The link uses an IP address instead of a normal domain.")
            score += 3

        # Suspicious URL keywords
        suspicious_url_words = [
            "login",
            "verify",
            "account",
            "secure",
            "update",
            "password"
        ]

        if any(word in link.lower() for word in suspicious_url_words):
            warnings.append("The link contains a potentially suspicious keyword.")
            score += 1

    # Check request for sensitive information
    sensitive_words = [
        "password",
        "otp",
        "credit card",
        "debit card",
        "bank account",
        "pin",
        "cvv"
    ]

    found_sensitive = []

    for word in sensitive_words:
        if word in email_text:
            found_sensitive.append(word)

    if found_sensitive:
        warnings.append(
            "The email asks for or mentions sensitive information: "
            + ", ".join(found_sensitive)
        )
        score += 3

    # Final classification
    if score >= 6:
        result = "HIGH RISK - POSSIBLE PHISHING"
    elif score >= 3:
        result = "MEDIUM RISK - BE CAREFUL"
    else:
        result = "LOW RISK - NO MAJOR RED FLAGS FOUND"

    return result, score, warnings


def display_result(result, score, warnings):

    print("\n" + "=" * 60)
    print("                 ANALYSIS RESULT")
    print("=" * 60)

    print("Risk Score:", score)
    print("Result    :", result)

    if warnings:
        print("\nRed Flags Found:")

        for number, warning in enumerate(warnings, start=1):
            print(f"{number}. {warning}")

    else:
        print("\nNo major phishing indicators were detected.")

    print("\nSafety Tips:")
    print("- Do not click suspicious links.")
    print("- Do not share passwords, OTPs or PINs.")
    print("- Verify the sender independently.")
    print("- Visit the official website by typing its address yourself.")
    print("- When in doubt, contact the organization directly.")


print("=" * 60)
print("             PHISHING EMAIL IDENTIFIER")
print("=" * 60)

sender = input("Sender email: ")
subject = input("Email subject: ")

print("\nEnter the email body.")
print("Type END on a new line when finished.")

body_lines = []

while True:
    line = input()

    if line == "END":
        break

    body_lines.append(line)

body = "\n".join(body_lines)

link = input("\nEnter suspicious link if present (or press Enter): ")

result, score, warnings = analyze_email(
    sender,
    subject,
    body,
    link
)

display_result(result, score, warnings)