#!/usr/bin/env python3
#
# REQUIREMENTS:
# THIS CBC REALISATION TAKING CYPHER FUNCTION AS A FUNCTION OF 2 ARGUMENTS
#   CYPHER: (BLOCK, KEY) -> CYPHERED_BLOCK
# THE BLOCK SIZE ARE FIXED: 128 BIT
#

import random


def split_to_blocks(plain_text, size=128):

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
    text = 0
    for i in range(len(blocks)):
        text += blocks[i] << size*i
    return text


def gen_initialize_vector(blocksize=128):
    return random.randint(0, 2**128)

def xor(cypher_text, plain_text):
    return cypher_text^plain_text

def encrypt(plain_text, key, encrypt_function):
    # blocks: [b,b,b,b,b]
    blocks = split_to_blocks(plain_text)
    iv = gen_initialize_vector()

    cypher = iv
    cyphered_blocks = [iv]

    for i in range(len(blocks)):
        cypher =xor(cypher, encrypt_function(blocks[i], key))
        cyphered_blocks.append(cypher)
    return unir(cyphered_blocks)

def decrypt(cypher_text, key, decrypt_function):
    blocks = split_to_blocks(cypher_text)
    iv = blocks[0]

    text_blocks = []
    for i in range(1,len(blocks)):
        text  = xor(blocks[i-1], decrypt_function(blocks[i],key))
        text_blocks.append(text)

    return unir(text_blocks)
