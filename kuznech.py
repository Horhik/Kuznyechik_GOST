#!/usr/bin/env python3

import cbc_mode.cypher as cbc
import argparse
from preprocessing import file_to_btext, file_write_btext
import keygen as k



parser = argparse.ArgumentParser(
    prog="Kuznech",
    description="The Kuznyechik 128-bit block cypher based on GOST R 34.12-2015. Implemented with cbc encryption mode"
)
parser.add_argument("-e", "--encrypt", action="store_true")
parser.add_argument("-d", "--decrypt", action="store_true")
parser.add_argument("-k", "--key", action="store")
parser.add_argument("-i", "--input", action="store")
parser.add_argument("-t", "--text", action="store")
parser.add_argument("-o", "--output", action="store")
parser.add_argument("--no-key", action="store_true")
args = parser.parse_args()

key = None
if args.no_key or not args.key:
    key = k.generate_main_key()
    k.write_key_to_file("default_key.txt", key)

elif args.key:
    key = k.read_key_from_file(args.key)

if args.encrypt and args.input and args.o:
    path = args.input
    content = file_to_btext(path)
    enc = cbc.cbc_encrypt_btext(content, key)
    file_write_btext(args.o, enc)

elif args.decrypt and args.input and args.o:
    path = args.input
    content = file_to_btext(path)
    dec = cbc.cbc_decrypt_btext(content, key)
    file_write_btext(args.o, dec)

elif args.encrypt and args.text:
    enc = cbc.cbc_encrypt_utf8(args.text, key)
    print(enc)

elif args.decrypt and args.text:
    dec = cbc.cbc_decrypt_utf8(args.text, key)
    print(dec)


else:
    print("Wrong options")
