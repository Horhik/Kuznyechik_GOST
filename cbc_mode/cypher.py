#!/usr/bin/env python3


from cypher import encrypt, decrypt
from preprocessing import encode, decode
import cbc_mode.cbc as cbc
from keygen import generate_main_key



def cbc_encrypt_utf8(text, key=None):
    if key == None:
        key = generate_main_key()


    encoded = encode(text)
    encrypted = cbc.encrypt(encoded, key)
    #btext = encrypted.to_bytes((encrypted.bit_length() + 7) // 8, "big")
    text = decode(encrypted)


    return (text, key)

def cbc_decrypt_utf8(text, key):
    numeric = int.from_bytes(text, "big")
    decrypted = cbc.decrypt(numeric, key)
    decoded = decode(decrypted)
    return decoded

def cbc_encrypt_btext(btext, key=None):
    if key == None:
        key = generate_main_key()


    numeric = int.from_bytes(btext, "big")
    encrypted = cbc.encrypt(numeric, key)
    btext = encrypted.to_bytes((encrypted.bit_length() + 7) // 8, "big")

    return (btext, key)

def cbc_decrypt_btext(btext, key):
    numeric = int.from_bytes(btext, "big")
    decrypted = cbc.decrypt(numeric, key)
    btext = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return btext
