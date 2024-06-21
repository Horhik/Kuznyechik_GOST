#!/usr/bin/env python3


from basic import split, ring_to_string
from transforms import L_transform, F_transform
from random import randint


def generate_constants():

    C = [] # 32 iterative constans
    for i in range(1, 33):
        # generating C_i constant
        C.append(L_transform(ring_to_string(i)))
    return C

def generate_main_key(seed=None):
    """ -> 256 bit """
    return randint(0, 2**256)

def split_key(key):
    """" V256 -> (V128, V128)"""

    return key >> 128, (key >> 128) << 128 ^ key

def F_recursion(i, key_prev, key_next, constants):
    result = (key_prev, key_next)
    for n in range(8*(i - 1), 8*(i - 1) + 8):
        result = F_transform(result, key=constants[n])
    return result


def iterative_key_generation(key, constants):
    k = [None]*10
    k[0], k[1] = split_key(key)

    for i in range(1, 4 + 1):
        k[2*i+1 + (-1)], k[2*i+2 + (-1)] = F_recursion(i, k[2*i-1 + (-1)], k[2*i + (-1)], constants)
    return k

def generate_keys(mainkey):
    constants = generate_constants()
    keys = iterative_key_generation(mainkey, constants)
    return keys


def write_key_to_file(path, key):# writing key to file
    # opening the file and writing key as bytes################################
    f = open(path, "wb")
    f.write(bytes(key))
    f.close()

def read_key_from_file(path):
    # opening the file and reading key as bytes
    f = open(path, "rb")
    key = f.read()
    f.close()
    key_as_int = int.from_bytes(key, "big")
    return key_as_int
