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
