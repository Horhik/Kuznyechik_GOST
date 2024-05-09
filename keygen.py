#!/usr/bin/env python3


def generate_constants():

    C = [] # 32 iterative constans
    for i in range(1, 33):
        # generating C_i constant
        C.append(L_transform(ring_to_string(i)))
    return C

def generate_main_key(seed):
    """ -> 256 bit """
    pass

def split_key(key):
    """" V256 -> (V128, V128)"""

    return key[128:126], key[0:128]

def F_recursion(i, key_prev, key_next, constants):
    result = (key_prev, key_next)
    for n in range(8*(i - 1), 8*(i - 1) + 8):
        result = F_transform(result, key=constants[n])


def iterative_key_generation(key, constants):
    k = [None]*10
    k[0], k[1] = split_key(key)

    for i in range(1, 4 + 1):
        k[2*i+1 + (-1)], k[2*i+2 + (-1)] = F_recursion(i, k[2*i-1 + (-1)], k[2*i + (-1)], constants)
