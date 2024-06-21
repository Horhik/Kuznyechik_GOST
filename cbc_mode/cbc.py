#!/usr/bin/env python3
#
# REQUIREMENTS:
# THIS CBC REALISATION TAKING CYPHER FUNCTION AS A FUNCTION OF 2 ARGUMENTS
#   CYPHER: (BLOCK, KEY) -> CYPHERED_BLOCK
# THE BLOCK SIZE ARE FIXED: 128 BIT
#

import random
import cypher as c


def split_to_blocks(plain_text, size=128):

    """
    N*V128
    a0||a1||...||a16 ->
    [a16, a15, ..., a1, a0]
    """

    length = len(bin(plain_text)[2:])
    text = plain_text
    blocks = []
    while text:
        # 101010 -> 101
        shift = text >> size

        #print("SHIFT: ", bin(shift)[2:])
        # 101010 ^ (101 -> 101000) -> 101010 ^ 101000 -> 010
        # push 010 to the end of the array

        blocks.append(text^(shift << size))
        #print("PUSHED: ", bin(blocks[-1])[2:])
        # 101010 -> 101
        text = shift
    return blocks

def unir(blocks,size=128):
    """
    [a16, a15, ..., a1, a0] ->
    a16 + a15 000 = a15 a16
    a15 a16 + a14 000 00 = a14 a15 a16
    ...
    a0 a1 ... a15 a16
    """

    text = 0
    for i in range(len(blocks)):
        text += blocks[i] << size*i
    return text


def gen_initialize_vector(blocksize=128):
    return random.randint(0, 2**128)

def xor(cypher_text, plain_text):
    return cypher_text^plain_text

def encrypt(plain_text, key):
    """
    T1 T2 T3
    T1, T2, T3
    C1 = IV + cypher(T1)
    C2 = C1 + cypher(T2)
    C3 = C2 + cypher(T3)

    IV, C1, C2, C3


    C3 C2 C1 IV


    cypher(T1) = C1 + IV
    cypher(T2) = C1 + C2
    cypher(T3) = C2 + C3
    """

    #
    blocks = list(reversed(split_to_blocks(plain_text)))
    iv = gen_initialize_vector()

    cypher = iv
    cyphered_blocks = [iv]


    for i in range(len(blocks)):
        cypher =xor(cypher, c.encrypt(blocks[i], key))
        cyphered_blocks.append(cypher)
    return cyphered_blocks

def decrypt(cypher_text, key):
    """"
    C3 C2 C1 IV

    C1 = IV + cypher(T1)
    C2 = C1 + cypher(T2)
    C3 = C2 + cypher(T3)

    IV, C1, C2, C3

    T1 = decrypt(C1 + IV)
    T2 = decrypt(C2 + C1)
    T3 = decrypt(C2 + C3)

    T1 T2 T3
    ->
    T1 T2 T3

    """
    # C1 C2 C3 IV -> IV C3 C2 C1
    # IV C1 C2 C3
    blocks = cypher_text #list(reversed(split_to_blocks(cypher_text)))
    iv = blocks[0]

    text_blocks = []
    for i in range(1,len(blocks)):
        text = c.decrypt(xor(blocks[i-1],blocks[i]),key)
        text_blocks.append(text)
    # T1 T2 T3
    text_blocks = list(reversed(text_blocks))
    return unir(text_blocks)
