def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher.

    Args:
        text (str): The input string to be encrypted or decrypted.
        shift (int): The number of positions to shift each character.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The processed (encrypted or decrypted) string.
    """
    result = ""
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def main():
    """
    Main function to interact with the user for Caesar Cipher operations.
    """
    print("Caesar Cipher Encryption/Decryption Tool")
    print("---------------------------------------")

    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? (e/d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")

    text = input("Enter the text: ")

    while True:
        try:
            shift = int(input("Enter the shift key (an integer): "))
            break
        except ValueError:
            print("Invalid shift key. Please enter an integer.")

    if mode == 'e':
        processed_text = caesar_cipher(text, shift, 'encrypt')
        print(f"\nEncrypted text: {processed_text}")
    else:
        processed_text = caesar_cipher(text, shift, 'decrypt')
        print(f"\nDecrypted text: {processed_text}")

    print("\nThank you for using the Caesar Cipher tool!")

if __name__ == "__main__":
    main()
