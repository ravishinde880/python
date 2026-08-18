def caesar_cipher(text, shift):
    result = ""

    for char in text:

        # Uppercase letters
        if char.isupper():
            new_position = (ord(char) - ord('A') + shift) % 26
            result += chr(new_position + ord('A'))

        # Lowercase letters
        elif char.islower():
            new_position = (ord(char) - ord('a') + shift) % 26
            result += chr(new_position + ord('a'))

        # Numbers, spaces and symbols remain unchanged
        else:
            result += char

    return result


def encrypt(text, key):
    return caesar_cipher(text, key)


def decrypt(text, key):
    return caesar_cipher(text, -key)


print("=" * 50)
print("       CAESAR CIPHER ENCRYPTION TOOL")
print("=" * 50)

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        message = input("Enter text to encrypt: ")

        try:
            key = int(input("Enter shift key (0-25): "))

            if key < 0 or key > 25:
                print("Please enter a key between 0 and 25.")
                continue

            encrypted_text = encrypt(message, key)

            print("\nOriginal Text :", message)
            print("Shift Key     :", key)
            print("Encrypted Text:", encrypted_text)

        except ValueError:
            print("Invalid key. Please enter a number.")

    elif choice == "2":

        message = input("Enter text to decrypt: ")

        try:
            key = int(input("Enter shift key (0-25): "))

            if key < 0 or key > 25:
                print("Please enter a key between 0 and 25.")
                continue

            decrypted_text = decrypt(message, key)

            print("\nEncrypted Text:", message)
            print("Shift Key     :", key)
            print("Decrypted Text:", decrypted_text)

        except ValueError:
            print("Invalid key. Please enter a number.")

    elif choice == "3":
        print("\nThank you for using Caesar Cipher!")
        break

    else:
        print("Invalid choice. Please select 1, 2 or 3.")