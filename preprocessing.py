#!/usr/bin/env python3

def encode(text, encoding="utf-8", endian="big"):
    return int.from_bytes(text.encode(encoding=encoding), endian)
