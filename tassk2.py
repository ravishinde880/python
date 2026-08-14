def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Preserve uppercase/lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Shift the character and wrap around the alphabet
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            # Keep spaces, numbers and punctuation unchanged
            result += char

    return result


print("=== Caesar Cipher Encryption Tool ===")

text = input("Enter your text: ")

try:
    shift = int(input("Enter the shift value: "))
except ValueError:
    print("Please enter a valid number for the shift.")
    exit()

encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("\nOriginal Text :", text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)