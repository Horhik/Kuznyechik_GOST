#!/usr/bin/env python3

def encode(text, encoding="utf-8", endian="big"):
    return int.from_bytes(text.encode(encoding=encoding), endian)

def decode(text, encoding="utf-8", endian="big"):
    btext = text.to_bytes((text.bit_length() + 7) // 8, endian)
    text = btext.decode(encoding=encoding)
    return text
