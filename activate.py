import logging

from script_ip import scan_local_network
from cryptography.fernet import Fernet
from encrypt_script import encrypt_address
import pickle

# Setup
ip_range = "192.168.1.0/24"  # Define subnet interface

active_devices = scan_local_network(ip_range)

# Key generator

def generate_shared_key():
    # Generates a shared secret key (this should be securely shared between parties)
    return Fernet.generate_key()


#  Encrypt the data using the encrypt method we created
def encrypt(active_devices):
    encrypted_dict = {}
    i = 0

    for device in active_devices:

        logging.info("DEVICE:", device)
        i += 1
        shared_key = generate_shared_key()
        ip = device['ip']
        mac = device['mac']
        encrypted_ip = encrypt_address(ip, shared_key)
        encrypted_mac = encrypt_address(mac, shared_key)
        encrypted = {'ip': encrypted_ip, 'mac': encrypted_mac}
        encrypted_dict[i] = {'address': encrypted, 'key': shared_key}

    logging.info(encrypted_dict)
    return encrypted_dict


#  Create a value to store the dict
encrypt_text = encrypt(active_devices)


#  Transform the dict into a binary file
def write_to_file(encrypt_text, file_path):
    # Serialize the dictionary into binary file
    encrypted_binary = pickle.dumps(encrypt_text)

    # Write the binary into a file
    with open(file_path, 'wb') as file:
        file.write(encrypted_binary)


#  We generate a file to store the encryption paired with keys, this is for simulate a communication
#  Should not be used since is kinda insecure
file_path = 'path'
write_to_file(encrypt_text, file_path)
