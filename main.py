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

def encrypt(text, keys):

    """ V128 -> V128"""

    cypher = text
    for i in range(0, 9):
        cypher = LSX_transform(cypher, keys[i])
    cypher = X_transform(cypher, keys[9])


def decrypt(cypher, keys):

    """ V128 -> V128"""

    text = cypher
    for i in range(9, 0, -1):
        cypher = LSX_transform_reversed(cypher, keys[i])
    cypher = X_transform(cypher, keys[0])

