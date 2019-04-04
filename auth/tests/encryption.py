from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

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


def encrypt_and_decrypt(message, file_name=PAIR_FILE_NAME):
    key = RSA.importKey(open(file_name, 'r').read())
    #key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
    decryptedtext = cipher.decrypt(ciphertext)

    print('-------------------------------')
    print('message: ', message)
    print('-------------------------------')
    print('ciphertext: ', ciphertext)
    print('-------------------------------')
    print('decryptedtext: ', decryptedtext.decode())
    print('-------------------------------')


if __name__ == '__main__':
    print('generate a new public key pair')
    generate_new_public_key_pair()

    print('encrypt and decrypt a message')
    encrypt_and_decrypt(b'Hello python!')
