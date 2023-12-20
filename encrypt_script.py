from cryptography.fernet import Fernet


#  Encrypting generator
def encrypt_address(device, key):
    cipher_suite = Fernet(key)
    encrypted_address = cipher_suite.encrypt(device.encode())
    return encrypted_address


#  Decrypting generator

def decrypt_address(device, key):
    cipher_suite = Fernet(key)
    decrypted_address = cipher_suite.decrypt(device).decode()
    return decrypted_address

