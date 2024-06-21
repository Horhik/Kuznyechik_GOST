#!/usr/bin/env python3

from cypher import encrypt, decrypt
from preprocessing import encode, decode
import cbc_mode.cbc as cbc
from keygen import generate_main_key


def cbc_encrypt(text, key=None):
    if key == None:
        key = generate_main_key()


    encoded = encode(text)
    encrypted = cbc.encrypt(encoded, key, encrypt)
    btext = encrypted.to_bytes((encrypted.bit_length() + 7) // 8, "big")

    return (btext, key, encoded)

def cbc_decrypt(text, key, eee):
    numeric = int.from_bytes(text, "big")
    print(eee)
    decrypted = cbc.decrypt(numeric, key, decrypt)
    print(decrypted)
    decoded = decode(decrypted)
    return decoded

message = "ПРИВ"
print("Message to encrypt", message)

e, key, eee = cbc_encrypt(message)

#print("Encrypted message: ", e)

#d = cbc_decrypt(e, key, eee)

#print("Decrypted message: ", e)
#print(d)


int_text = encode(message)
int_encrypted = encrypt(int_text, key)
int_decrypt = decrypt(int_encrypted,key)
str_decrypted = decode(int_decrypt)
print(str_decrypted)
