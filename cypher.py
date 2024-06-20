#!/usr/bin/env python3

"""
GOST definitions

V(*) = set of all finit-length strings of binary data, e.g. "0101010"

V(s) = set of all `s` - length strings of binary data

|A| = power of A

A ++ B = string concatenation. |A ++ B| = |A| + |B|

A <<<n or (<<<)(A, n) = cyclic shift of |A| == 32 to the side with bigger indexes

^: (Vs, Vs) -> Vs = XOR

Z(2^s): ring by 2^s

|+|:  (Z(2^32), Z(2^32)) -> Z(2^32)


"""

""" Basic encryption algorithm """

from keygen import generate_keys
from transforms import LSX_transform, X_transform, LSX_transform_reversed

def encrypt(text, key):

    """ V128 -> V128"""
    keys = generate_keys(key)
    cypher = text
    for i in range(0, 9):
        cypher = LSX_transform(cypher, keys[i])
    cypher = X_transform(cypher, keys[9])
    return cypher


def decrypt(cypher, key):

    """ V128 -> V128"""

    keys = generate_keys(key)
    text = cypher
    for i in range(9, 0, -1):
        text = LSX_transform_reversed(text, keys[i])
    text = X_transform(text, keys[0])
    return text
