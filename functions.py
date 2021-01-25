import hashlib
import math
import os

def aes_it(for_encryption):
    from Crypto.Cipher import AES
    IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
    KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
    SALT_SIZE = 16  # This size is arbitrary
    cleartext = for_encryption
    password = b'j54uPq15XB&jhR>j'
    salt = os.urandom(SALT_SIZE)
    derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                  dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]
    encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)
    return encrypted



def deaes_it(encrypted):
    from Crypto.Cipher import AES
    IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
    KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
    SALT_SIZE = 16  # This size is arbitrary
    password = b'j54uPq15XB&jhR>j'
    salt = encrypted[0:SALT_SIZE]
    derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
    iv = derived[0:IV_SIZE]
    key = derived[IV_SIZE:]
    cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])
    return cleartext
