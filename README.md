# Ransom-Simulation

This script provides functionality for file encryption and decryption using the cryptography library, specifically the `Fernet module`


## 1. Importing Required Module
```
from cryptography.fernet import Fernet
```
The `cryptography.fernet` module provides methods for secure symmetric encryption and decryption.


## 2. Generate and Save a Key
```
def generate_key(key_file):
    key = Fernet.generate_key()  # Generates a secure, random key
    with open(key_file, 'wb') as key_out:
        key_out.write(key)  # Saves the key to a file
    print(f"Key saved to {key_file}")
```
* Purpose: Generates a symmetric encryption key and saves it to a file.
* How It Works:
    * `Fernet.generate_key()` creates a random encryption key.
    * The key is written to a specified file (`key_file`) in binary mode (`'wb'`).


## 3. Load a Key from a File
```
def load_key(key_file):
    with open(key_file, 'rb') as key_in:
        return key_in.read()  # Reads and returns the key from the file
```
* Purpose: Reads an encryption key from a file.
* How It Works:
    * Opens the key file in binary mode (`'rb'`).
    * Reads and returns the stored key.


## 4. Encrypt a File
```
def encrypt_file(input_file, encrypted_file, key):
    fernet = Fernet(key)  # Initializes Fernet with the given key
    with open(input_file, 'rb') as file_in:
        data = file_in.read()  # Reads the contents of the input file
        encrypted_data = fernet.encrypt(data)  # Encrypts the data
    with open(encrypted_file, 'wb') as file_out:
        file_out.write(encrypted_data)  # Saves the encrypted data to a new file
    print(f"File encrypted as {encrypted_file}")
```
* Purpose: Encrypts the contents of a file.
* How It Works:
    * The key initializes a `Fernet` object for encryption.
    * The input file is read in binary mode.
    * The file's contents are encrypted using `fernet.encrypt()`.
    * The encrypted data is saved to a new file.
 

## 5. Decrypt a File
```
def decrypt_file(encrypted_file, decrypted_file, key):
    fernet = Fernet(key)  # Initializes Fernet with the given key
    with open(encrypted_file, 'rb') as file_in:
        encrypted_data = file_in.read()  # Reads the encrypted file
        decrypted_data = fernet.decrypt(encrypted_data)  # Decrypts the data
    with open(decrypted_file, 'wb') as file_out:
        file_out.write(decrypted_data)  # Saves the decrypted data to a new file
    print(f"File decrypted as {decrypted_file}")
```
* Purpose: Decrypts an encrypted file back to its original content.
* How It Works:
    * Similar to encryption, but uses `fernet.decrypt()` to decode the encrypted data.
    * The decrypted data is saved to a new file.
 

## 6. Example Usage
```
if __name__ == "__main__":
    key_file = "key.key"
    generate_key(key_file)  # Generate and save the key

    key = load_key(key_file)  # Load the saved key

    input_file = "example.txt"
    encrypted_file = "example.encrypted"
    decrypted_file = "example_decrypted.txt"

    encrypt_file(input_file, encrypted_file, key)  # Encrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)  # Decrypt the file
```
* Purpose: Demonstrates the script functionality.
* Steps:
    1. Generate and save an encryption key to `key.key`.
    2. Load the saved key.
    3. Specify the input file (`example.txt`) for encryption.
    4. Encrypt the input file and save it as `example.encrypted`.
    5. Decrypt `example.encrypted` and save the original content as `example_decrypted.txt`.
 

## Workflow Summary:
1. **Key Generation** : A key is generated and saved to `key.key`.
2. **Encryption**: The contents of `example.txt` are read and encrypted using the key, producing `example.encrypted`.
3. **Decryption**: The encrypted file `example.encrypted` is decrypted using the same key, recovering the original content in `example_decrypted.txt`.

