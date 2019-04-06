import json
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
import base64

PUBLIC_FILE_NAME = 'public.pem'
PAIR_FILE_NAME = 'pair.pem'


def generate_new_public_key_pair(pair_file_name=PAIR_FILE_NAME, public_file_name=PUBLIC_FILE_NAME, size=2048):
    key = RSA.generate(size)
    public_key = key.publickey()

    with open(public_file_name, 'wb') as public_file:
        public_file.write(public_key.exportKey('PEM'))

    with open(pair_file_name, 'wb') as pair_file:
        pair_file.write(key.exportKey('PEM'))


def read_key(file_name):
    with open(file_name, 'r') as key_file:
        return RSA.importKey(key_file.read())


def server_public_key():
    return RSA.importKey(open(os.path.dirname(os.path.abspath(__file__))+'/public.pem', 'r').read())


def server_key_pair():
    return RSA.importKey(open(os.path.dirname(os.path.abspath(__file__))+'/pair.pem', 'r').read())


def encrypt_and_decrypt_server(message, file_name=PAIR_FILE_NAME):
    return encrypt_and_decrypt(message, RSA.importKey(open(file_name, 'r').read()))


def decrypt(message, key):
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(base64.b64decode(message))
    return decrypted_message


def encrypt(message, key):
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message)
    return base64.b64encode(encrypted_message)


def encrypt_and_decrypt(message, key):
    #key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)

    b64_message = base64.b64encode(ciphertext)
    print('b64_message: ', b64_message)
    b64_decoded_message = b64_message.decode()
    print('b64_decoded_message: ', b64_decoded_message)
    b64_message2 = b64_decoded_message.encode()
    print('b64_message2: ', b64_message2)
    ciphertext2 = base64.b64decode(b64_message2)
    print('ciphertext2: ', ciphertext2)

    decryptedtext = cipher.decrypt(ciphertext2)

    print('-------------------------------')
    print('message: ', message)
    print('-------------------------------')
    print('ciphertext: ', ciphertext)
    print('-------------------------------')
    print('decryptedtext: ', decryptedtext.decode())
    print('-------------------------------')


if __name__ == '__main__':
    print('* generate a new public key pair')
    #generate_new_public_key_pair()
        
    encrypt_and_decrypt(b'hello world!', RSA.generate(2048))

    #print('* encrypt and decrypt a message')
    #encrypt_and_decrypt_server(b'{"SERVER_KEY": "hello there key"}')
