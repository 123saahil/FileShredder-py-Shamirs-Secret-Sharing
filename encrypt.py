# encrypt.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, key):
    """
    Encrypt the file using AES encryption.
    """
    with open(file_path, 'rb') as file:
        data = file.read()

    # Create AES cipher and encrypt the data
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Write encrypted data to a new file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(cipher.iv)  # Save IV to the file
        encrypted_file.write(encrypted_data)

    return encrypted_file_path

