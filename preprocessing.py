#!/usr/bin/env python3

# text to int number
def encode(text, encoding="utf-32", endian="big"):
    return int.from_bytes(text.encode(encoding), endian)

# int number to text
def decode(numeric, encoding="utf-32", endian="big"):
    btext = numeric.to_bytes((numeric.bit_length() + 7) // 8, endian)
    return btext.decode(encoding)
def file_to_btext(path):
    f = open(path, mode="rb")
    data = f.read()
    return data

def file_write_btext(path, btext):
    f = open(path, "wb")
    f.write(btext)
