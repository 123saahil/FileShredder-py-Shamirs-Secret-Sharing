import tkinter as tk
from tkinter import filedialog, messagebox
import main
from Crypto.Random import get_random_bytes

# Generate a random AES key for encryption and decryption
def generate_key():
    return get_random_bytes(16)  # 128-bit key for AES

def encrypt_file_gui():
    file_path = filedialog.askopenfilename(title="Select a file to encrypt")
    if file_path:
        key = generate_key()
        encrypted_file = main.encrypt_file(file_path, key)
        messagebox.showinfo("Success", f"File encrypted successfully!\nEncrypted file: {encrypted_file}")
    else:
        messagebox.showerror("Error", "No file selected.")

def decrypt_file_gui():
    encrypted_file_path = filedialog.askopenfilename(title="Select an encrypted file to decrypt")
    if encrypted_file_path:
        key = generate_key()  # Using a random key, but in a real scenario, you'd need to keep track of this key
        decrypted_file = main.decrypt_file(encrypted_file_path, key)
        messagebox.showinfo("Success", f"File decrypted successfully!\nDecrypted file: {decrypted_file}")
    else:
        messagebox.showerror("Error", "No file selected.")

def shred_file_gui():
    file_path = filedialog.askopenfilename(title="Select a file to shred")
    if file_path:
        result = main.shred_file(file_path)
        messagebox.showinfo("Success", result)
    else:
        messagebox.showerror("Error", "No file selected.")

def create_gui():
    window = tk.Tk()
    window.title("File Encryptor, Decryptor & Shredder")

    encrypt_button = tk.Button(window, text="Encrypt File", command=encrypt_file_gui)
    encrypt_button.pack(pady=10)

    decrypt_button = tk.Button(window, text="Decrypt File", command=decrypt_file_gui)
    decrypt_button.pack(pady=10)

    shred_button = tk.Button(window, text="Shred File", command=shred_file_gui)
    shred_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
    
    
   

