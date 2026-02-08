import os
import argparse
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=1000000)

def encrypt_file(input_file: str, password: str, keyfile: str = None) -> None:
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    
    cipher = AES.new(key, AES.MODE_GCM)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(pad(plaintext, AES.block_size))

    with open(input_file + '.enc', 'wb') as f:
        f.write(salt + cipher.nonce + tag + ciphertext)

def decrypt_file(encrypted_file: str, password: str) -> None:
    with open(encrypted_file, 'rb') as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    try:
        plaintext = unpad(cipher.decrypt_and_verify(ciphertext, tag), AES.block_size)
    except (ValueError, KeyError):
        print("Decryption failed or verification failed!")

    with open(encrypted_file[:-4], 'wb') as f:
        f.write(plaintext)

def generate_keyfile(password: str, keyfile_path: str) -> None:
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    with open(keyfile_path, 'wb') as f:
        f.write(salt + key)

def main():
    parser = argparse.ArgumentParser(description="File Encryption Tool")
    parser.add_argument('--encrypt', metavar='input_file', type=str, help='File to encrypt')
    parser.add_argument('--decrypt', metavar='encrypted_file', type=str, help='File to decrypt')
    parser.add_argument('--password', type=str, required=True, help='Password for encryption/decryption')
    parser.add_argument('--keyfile', type=str, help='Keyfile for encryption/decryption')

    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.encrypt, args.password, args.keyfile)
    elif args.decrypt:
        decrypt_file(args.decrypt, args.password)

if __name__ == '__main__':
    main()