from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(encrypted_file_path, key):
    """
    Decrypt the encrypted file using AES and handle padding properly.
    """
    with open(encrypted_file_path, 'rb') as encrypted_file:
        iv = encrypted_file.read(16)  # The first 16 bytes are the IV
        encrypted_data = encrypted_file.read()

    # Ensure the key is in the correct format for AES (length should be 16 bytes)
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key length must be 16, 24, or 32 bytes.")

    # Create AES cipher and decrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    except ValueError:
        raise ValueError("PKCS#7 padding is incorrect. Possibly due to using the wrong key.")

    # Write decrypted data to a new file
    decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

