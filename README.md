# Cybersecurity Week 1: AES Encryption and Password Hashing

This repository contains code examples and implementations for basic cryptography concepts as part of the Week 1 tasks in a cybersecurity internship.

## Overview

- Implemented AES encryption and decryption to securely transform plaintext.
- Implemented password hashing using secure algorithms (e.g., bcrypt) for safely storing passwords.
- Demonstrates how to use cryptography libraries in Python.

## Features

- Encrypt and decrypt strings using AES symmetric encryption.
- Hash passwords securely to protect user credentials.
- Simple Python scripts with clear, commented code.

## Requirements

- Python 3.x
- `cryptography` library (`pip install cryptography`)
- `bcrypt` library (`pip install bcrypt`)

## Usage

1. Clone this repository:


git clone https://github.com/helina0910/cybersecurity-week1.git

2. Navigate into the project directory:\

cd cybersecurity-week1

3. Install dependencies:

pip install -r requirements.txt

*(If you don’t have a requirements file, install manually as mentioned above)*

4. Run the encryption or hashing scripts as needed.

## Sample Code

```python
# Example AES encryption/decryption snippet
from cryptography.fernet import Fernet

# Generate key and save securely
key = Fernet.generate_key()
cipher = Fernet(key)

encrypted = cipher.encrypt(b"Secret Message")
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted.decode())

Author
Helen Roja Kakumanu

