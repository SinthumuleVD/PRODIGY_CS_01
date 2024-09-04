def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse the text
    for char in text:
        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char

    return result

def main():
    # Get user input for the message, shift value, and mode (encrypt/decrypt)
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Do you want to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): ").lower()

    # Validate mode input
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
        return

    # Perform the Caesar Cipher encryption/decryption
    result = caesar_cipher(message, shift, mode)

    # Display the result
    print(f"The {mode}ed message is: {result}")

if __name__ == "__main__":
    main()
