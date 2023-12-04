
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# def encrypt_message(message, key):
#     # Encrypt the message using the key
#     encrypted_message = message + key
#     return encrypted_message

def authenticate_and_decrypt_message(encrypted_message, key):
    # Authenticate the encrypted message using the key
    authenticated = False
    if encrypted_message.endswith(key):
        authenticated = True

    # Decrypt the message if authenticated
    if authenticated:
        decrypted_message = encrypted_message[:-len(key)]
        return decrypted_message
    else:
        return "Authentication failed"


def encrypt_message(message, key, algorithm):
    backend = default_backend()
    iv = b'\x00' * 16  # Initialization vector (IV) for AES and DES
    padder = padding.PKCS7(algorithm.block_size).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithm(key.encode()), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

    return encrypted_message

def decrypt_message(encrypted_message, key, algorithm):
    backend = default_backend()
    iv = b'\x00' * 16  # Initialization vector (IV) for AES and DES

    cipher = Cipher(algorithm(key.encode()), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithm.block_size).unpadder()
    unpadded_message = unpadder.update(decrypted_message) + unpadder.finalize()

    return unpadded_message.decode()

# Example usage
message = "Hello, world!"
key = "secret_keydjdjjdjjdjdjjdjjddjdjjdjdjdjdjjdjdjdjjdjdjjdjjdjjdjdjdjddjjjjdjdjdj"

aes_encrypted_message = encrypt_message(message, key, algorithms.AES)
print("AES Encrypted message:", aes_encrypted_message)

aes_decrypted_message = decrypt_message(aes_encrypted_message, key, algorithms.AES)
print("AES Decrypted message:", aes_decrypted_message)

des_encrypted_message = encrypt_message(message, key, algorithms.TripleDES)
print("DES Encrypted message:", des_encrypted_message)

des_decrypted_message = decrypt_message(des_encrypted_message, key, algorithms.TripleDES)
print("DES Decrypted message:", des_decrypted_message)

sha256_hash = hashlib.sha256(message.encode()).hexdigest()
print("SHA256 Hash:", sha256_hash)


# Example usage
message = "Hello, world!"
key = "secret_key"

# encrypted_message = encrypt_message(message, key)
# print("Encrypted message:", encrypted_message)

# decrypted_message = authenticate_and_decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)

from cryptography.fernet import Fernet
>>> Fernet.generate_key()


Fernet.generate_key()

fernet = Fernet(b'6CP0ErGC3SG7H_OQ_n9CVXwDrdXa7kvn4Q53UwI_giE=')

fernet.encrypt(b'1') 