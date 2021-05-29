alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'  # "abcdefghijklmnopqrstuvwxyz"


def decrypt():
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % len(alphabet)
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n")
    print("Stand by, almost finished...\n")
    print("Your decrypted message is:\n")
    print(decrypted_message)


decrypt()
