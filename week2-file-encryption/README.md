# Week 2 File Encryption Tool

## Features
- **AES-256-GCM**: A secure encryption standard.
- **PBKDF2 Key Derivation**: To securely derive keys from passwords.
- **Password Verification**: Ensures correct user authentication.
- **Key File Support**: Allows the use of external files for encryption keys.

## Usage Examples

### Encrypting a File
```bash
./encrypt_tool --input myfile.txt --output myfile.enc --password mypassword
```

### Decrypting a File
```bash
./decrypt_tool --input myfile.enc --output myfile.txt --password mypassword
```

### Using Key Files
```bash
./encrypt_tool --input myfile.txt --output myfile.enc --keyfile keyfile.key
./decrypt_tool --input myfile.enc --output myfile.txt --keyfile keyfile.key
```

## Key Management Best Practices
1. Use strong passwords and change them regularly.
2. Store key files securely and limit access.
3. Regularly update encryption software to the latest version.

## Requirements
- Python 3.6+
- Libraries: PyCryptodome, argparse, etc.