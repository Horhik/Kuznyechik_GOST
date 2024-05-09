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

""" Tables for nonlinear transformations """

# S block
""" Transformations """

def X_transform(string_128, key=None):
    return xor(key, string)

def S_tranform(string):

    """ V128 -> V128 """

    array = split(string, 16)
    array = nonlinear_transform(a)
    return np.hstack(array)

def S_transform_reversed(string):

    """ V128 -> V128 """

    array = split(string, 16)
    array = nonlinear_transform_reversed(a)
    return np.hstack(array)

def R_transform(string):
    array = split(string, 16)
    new_string = linear_transform(array)
    return np.hstack(new_string, array[:-1])

def L_transform(string):
    return compose_n_times(R_transform, string, 16)

def R_transform_reversed(string):
    array = split(string, 16)
    without_first = array[1:]
    return np.hstack(without_first, linear_transform(np.hstack(without_first, array[0])))

def L_transform_reversed(string):
    return compose_n_times(R_transform_reversed, string, 16)

def F_transform(two_strings, key):

    v128_1, v128_0 = two_strings
    return (xor(L_transform(S_tranform(X_transform(v128_1, key=key))), v128_0), v128_0)

def LSX_transform(string_128, key):
    return L_transform(S_tranform(X_transform(string_128, key=key)))

def LSX_transform_reversed(string_128, key):
    return S_transform_reversed(L_transform_reversed(X_transform(string_128, key=key)))

""" Key expanding algorithms """

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


def feistel_process_block(block, process_function, key):
    L, R = split(block)
    X = process_function(L, key)
    X = xor(X, R)

print(len(S))
