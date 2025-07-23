# ramcharan-vemulacaesar-cipher-using-python
# Caesar Cipher Encryption/Decryption Tool

This is a simple Python script that implements the classic Caesar Cipher, one of the oldest and simplest encryption techniques. It allows users to encrypt or decrypt text messages using a specified shift key.

## Features

* **Encryption:** Encrypts a given text using a positive shift key.
* **Decryption:** Decrypts an encrypted text using the original shift key (or its negative equivalent).
* **Case-Preserving:** Maintains the case of letters (uppercase remains uppercase, lowercase remains lowercase).
* **Non-Alphabetic Character Handling:** Non-alphabetic characters (numbers, symbols, spaces) are left unchanged.
* **User-Friendly Interface:** Simple command-line interface for input and output.

## How it Works

The Caesar Cipher works by shifting each letter in the plaintext a certain number of places down or up the alphabet. For example, with a left shift of 3, D would become A, E would become B, and so on.

## Getting Started

### Prerequisites

* Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository (or download the files):**
    ``bash
    git clone [https://github.com/ramcharan-vemulapudi/caesar-cipher-python.git](https://github.com/ramcharan-vemulapudi/caesar-cipher-python.git).
    cd caesar-cipher-python
    ``

2.  Alternatively, you can manually create the `caesar_cipher.py` and `README.md` files in a new directory and copy the code into them.

### Usage

1.  **Run the script:**
    ```bash
    python caesar_cipher.py
    ```

2.  **Follow the prompts:**
    * Choose whether to `(e)ncrypt` or `(d)ecrypt`.
    * Enter the text you want to process.
    * Enter the integer shift key.

**Example Encrypt:**
I cannot directly create and upload a project to your GitHub. However, I can provide you with the full Python code for a Caesar Cipher encryption/decryption tool, along with explanations and instructions on how to set it up and use it, which you can then upload to your GitHub.

This project will include:

Python Code (caesar_cipher.py): A script that handles both encryption and decryption based on user input.

A README.md file: Explaining the project, how to run it, and its features.

Basic Usage Instructions: How to get this onto your GitHub.

Caesar Cipher Project
Here's the content for your GitHub project:

1. caesar_cipher.py
Python

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
2. README.md
Markdown

# Caesar Cipher Encryption/Decryption Tool

This is a simple Python script that implements the classic Caesar Cipher, one of the oldest and simplest encryption techniques. It allows users to encrypt or decrypt text messages using a specified shift key.

## Features

* **Encryption:** Encrypts a given text using a positive shift key.
* **Decryption:** Decrypts an encrypted text using the original shift key (or its negative equivalent).
* **Case-Preserving:** Maintains the case of letters (uppercase remains uppercase, lowercase remains lowercase).
* **Non-Alphabetic Character Handling:** Non-alphabetic characters (numbers, symbols, spaces) are left unchanged.
* **User-Friendly Interface:** Simple command-line interface for input and output.

## How it Works

The Caesar Cipher works by shifting each letter in the plaintext a certain number of places down or up the alphabet. For example, with a left shift of 3, D would become A, E would become B, and so on.

## Getting Started

### Prerequisites

* Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/caesar-cipher-python.git](https://github.com/YOUR_USERNAME/caesar-cipher-python.git)
    cd caesar-cipher-python
    ```
    (Replace `YOUR_USERNAME` with your actual GitHub username and adjust the repository name if you choose a different one.)

2.  Alternatively, you can manually create the `caesar_cipher.py` and `README.md` files in a new directory and copy the code into them.

### Usage

1.  **Run the script:**
    ```bash
    python caesar_cipher.py
    ```

2.  **Follow the prompts:**
    * Choose whether to `(e)ncrypt` or `(d)ecrypt`.
    * Enter the text you want to process.
    * Enter the integer shift key.

**Example Encrypt:**

* Do you want to (e)ncrypt or (d)ecrypt? (e/d): e
* Enter the text: Hello, World!
* Enter the shift key (an integer): 3

* Encrypted text: Kelli, Zruog!
* Thank you for using the Caesar Cipher tool!

**Example Decrypt:**

* Do you want to (e)ncrypt or (d)ecrypt? (e/d): d
* Enter the text: Kelli, Zruog!
* Enter the shift key (an integer): 3

* Decrypted text: Hello, World!
* Thank you for using the Caesar Cipher tool!
