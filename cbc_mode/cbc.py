#!/usr/bin/env python3
#
# REQUIREMENTS:
# THIS CBC REALISATION TAKING CYPHER FUNCTION AS A FUNCTION OF 2 ARGUMENTS
#   CYPHER: (BLOCK, KEY) -> CYPHERED_BLOCK
# THE BLOCK SIZE ARE FIXED: 128 BIT
#

import random
import cypher as c
import sys


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
    (int, int) -> int
    T1 T2 T3
    T3, T2, T1
    C3 = IV + cypher(T3)
    C2 = C3 + cypher(T2)
    C1 = C2 + cypher(T1)

    IV, C3, C2, C1


    C1 C2 C3 IV
    """

    #
    blocks = split_to_blocks(plain_text)
    iv = gen_initialize_vector()

    cypher = iv
    cyphered_blocks = [iv]
    l = len(blocks)
    print("Total blocks: ", l)
    for i in range(len(blocks)):
        #print(f"Encrypting {i} block")

        print(f"{int(i/l*100)}% complete", end='\r')

        sys.stdout.flush()
        cypher =xor(cypher, c.encrypt(blocks[i], key))
        cyphered_blocks.append(cypher)
    return unir(cyphered_blocks)

def decrypt(cypher_text, key):
    """"
    C1 C2 C3 IV

    C3 = IV + cypher(T3)
    C2 = C3 + cypher(T2)
    C1 = C2 + cypher(T1)

    IV, C3, C2, C1

    T3 = decrypt(C3 + IV)
    T2 = decrypt(C3 + C2)
    T1 = decrypt(C2 + C1)

    T3,T2,T1
    ->
    T1 T2 T3

    """
    blocks = split_to_blocks(cypher_text)
    iv = blocks[0]
    l = len(blocks)
    text_blocks = []
    for i in range(1,l):
        print(f"{int(i/l*100)}% complete", end='\r')
        sys.stdout.flush()
        text  = c.decrypt(xor(blocks[i-1], blocks[i]),key)
        text_blocks.append(text)

    return unir(text_blocks)

'''
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
    plain_text: t0||t1||...||t16

    c16 = iv + enc(t16)
    c15 = c16 + enc(t15)

    ...
    c0 = c1 + enc(t0)
    """

    #blocks:  [t16, ..., t1, t0]
    blocks = split_to_blocks(plain_text)
    iv = gen_initialize_vector()

    cypher = iv
    # cyphered_blocks: [iv, c16, ..., c1, c0]
    cyphered_blocks = [iv]


    for i in range(len(blocks)):
        # cypher: c(i - 1) + c(i)
        cypher =xor(cypher, c.encrypt(blocks[i], key))
        cyphered_blocks.append(cypher)

    # cypher: c0||c1||...||c16||iv
    cypher = unir(cyphered_blocks)
    return cypher

def decrypt(cypher_text, key):

    blocks = split_to_blocks(cypher_text)

    text_blocks = 0
    for i in range(1,len(blocks)):
        text = c.decrypt(xor(blocks[i-1],blocks[i]),key)
        text_blocks ^= text << 2**(i - 1)
    # T1 T2 T3
    return text_blocks

'''
