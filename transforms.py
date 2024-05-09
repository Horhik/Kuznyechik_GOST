#!/usr/bin/env python3

import basic as b

""" Transformations """

def X_transform(string_128, key=None):
    """
    Simple XOR
    """
    return b.xor(key, string)

def S_transform(string):

    """ V128 -> V128 """

    array = b.split(string, 16)
    array = b.nonlinear_transform(a)

    return np.hstack(array)

def S_transform_reversed(string):

    """ V128 -> V128 """

    array = b.split(string, 16)
    array = b.nonlinear_transform_reversed(array)
    return np.hstack(array)

def R_transform(string):
    array = b.split(string, 16)
    new_string = b.linear_transform(array)
    return np.hstack(new_string, array[:-1])

def L_transform(string):
    return b.compose_n_times(R_transform, string, 16)

def R_transform_reversed(string):
    array = b.split(string, 16)
    without_first = array[1:]
    return np.hstack(without_first, b.linear_transform(np.hstack(without_first, array[0])))

def L_transform_reversed(string):
    return b.compose_n_times(R_transform_reversed, string, 16)

def F_transform(two_strings, key):

    v128_1, v128_0 = two_strings
    return (b.xor(L_transform(S_tranform(X_transform(v128_1, key=key))), v128_0), v128_0)

def LSX_transform(string_128, key):
    return L_transform(S_tranform(X_transform(string_128, key=key)))

def LSX_transform_reversed(string_128, key):
    return S_transform_reversed(L_transform_reversed(X_transform(string_128, key=key)))
