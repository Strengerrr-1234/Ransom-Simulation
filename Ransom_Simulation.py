from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as key_out:
        key_out.write(key)
    print(f"Key saved to {key_file}")

# Function to load a key from a file
def load_key(key_file):
    with open(key_file, 'rb') as key_in:
        return key_in.read()

# Function to encrypt a file
def encrypt_file(input_file, encrypted_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file_in:
        data = file_in.read()
        encrypted_data = fernet.encrypt(data)
    with open(encrypted_file, 'wb') as file_out:
        file_out.write(encrypted_data)
    print(f"File encrypted as {encrypted_file}")

# Function to decrypt a file
def decrypt_file(encrypted_file, decrypted_file, key):
    fernet = Fernet(key)
    with open(encrypted_file, 'rb') as file_in:
        encrypted_data = file_in.read()
        decrypted_data = fernet.decrypt(encrypted_data)
    with open(decrypted_file, 'wb') as file_out:
        file_out.write(decrypted_data)
    print(f"File decrypted as {decrypted_file}")

# Example usage
if __name__ == "__main__":
    key_file = "key.key"
    generate_key(key_file)  # Generate and save the key

    key = load_key(key_file)  # Load the saved key

    input_file = "example.txt"
    encrypted_file = "example.encrypted"
    decrypted_file = "example_decrypted.txt"

    encrypt_file(input_file, encrypted_file, key)  # Encrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)  # Decrypt the file
