# File Shredder Using Shamir's Secret Sharing

## Team Members
- **Saahil Mishra** (22BCS105)
- **Rohit** (22BCS100)
- **Shriya Udupa** (22BCS121)
- **Laxmi** (22BCS059)

---

## About the Project
The **File Shredder using Shamir's Secret Sharing** project is implemented in **Python**. It provides a secure tool for file encryption, shredding, and key distribution using **Shamir’s Secret Sharing Scheme (SSS)**. By combining AES encryption with SSS, the project ensures file security and enables secure key reconstruction with a predefined threshold of shares.

---

## Security Measures Implemented
1. **AES Encryption**: Encrypts the file contents to secure sensitive data.
2. **Shamir's Secret Sharing Scheme**: Splits the AES key into multiple shares, requiring a specific threshold (`k`) for reconstruction.
3. **File Shredding**: Securely deletes the original files by overwriting them, preventing recovery.

---

## Objectives
To create a Python-based tool that:
- Encrypts files using **AES encryption**.
- Splits the encryption key into multiple shares using **Shamir’s Secret Sharing Scheme**.
- Allows reconstruction of the AES key using a threshold number of shares (`k`).
- Securely shreds original files to prevent unauthorized recovery.

---

## Features
1. **File Encryption with AES**
   - Encrypt files using the AES algorithm (`pycryptodome`) to protect their contents.

2. **Shamir’s Secret Sharing Scheme**
   - Split the AES encryption key into shares using `secretsharing` or similar libraries.
   - Allow key reconstruction with a specific number (`k`) of shares.

3. **File Shredding**
   - Delete files securely by overwriting their data to prevent recovery.

4. **Key Reconstruction and File Decryption**
   - Decrypt files by:
     - Providing the encrypted file.
     - Supplying a minimum of `k` shares to reconstruct the AES key.

---

## Technologies Used
The project is implemented in **Python** and utilizes:
- **`pycryptodome`**: For AES encryption and decryption.
- **`secretsharing`**: For splitting and reconstructing the AES key.
- **`os` and `shutil`**: For secure file shredding.
- **`tkinter` or `PyQt5`** (Optional): For the graphical user interface.

---

## Project Structure
```plaintext
File-Shredder-SSS/
├── encrypt.py            # Handles AES encryption and decryption
├── share_secret.py       # Implements Shamir's Secret Sharing Scheme
├── shredder.py           # Provides secure file shredding functionality
├── main.py               # Executes encryption, sharing, shredding, and decryption workflows
├── gui.py                # Optional GUI implementation
├── requirements.txt      # List of required Python libraries
└── README.md             # Project documentation
