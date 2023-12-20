import logging
import os
import pickle

from encrypt_script import decrypt_address


file_path = 'path'

#  Transform the json file into a dict


def read_from_file(file_path):
    # Read a binary file
    with open(file_path, 'rb') as file:
        encrypted_binary = file.read()

    # Deserialize the content from binary to a dict
    encrypt_text = pickle.loads(encrypted_binary)

    return encrypt_text


#  Create a value to store the dict
read_encrypted_data = read_from_file(file_path)

#  Decrypt the data using the encrypt method we created

def decrypt(read_encrypted_data):
    i = 0
    decrypted_dict = {}
    for device in read_encrypted_data:
        i += 1
        encrypted_ip = device['address']['ip']
        encrypted_mac = device['address']['mac']
        key = device['key']
        decrypted_ip = decrypt_address(encrypted_ip, key)
        decrypted_mac = decrypt_address(encrypted_mac, key)
        decrypted = {'ip': decrypted_ip, 'mac': decrypted_mac}
        decrypted_dict[i] = {'address': decrypted, 'key': key}

    logging.info(decrypted_dict)
    return decrypted_dict


# After decryption, remove the encrypted file
os.remove(file_path)
