def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
message = input("Enter the message: ")
shift = int(input("Enter the shift value (e.g., 3): "))

choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("Encrypted message:", encrypted)
elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("Decrypted message:", decrypted)
else:
    print("Invalid option selected.")
