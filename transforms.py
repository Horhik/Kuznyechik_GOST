#!/usr/bin/env python3

import basic as b
import numpy as np

""" Transformations """

def X_transform(string_128, key=None):
    """
    Simple XOR
    """
    return b.xor(key, string_128)

def S_transform(string, N=16, size=8):

    """ V128 -> V128 """

    array = b.split(string, N)
    array = [b.nonlinear_transform(array[i]) for i in range(N - 1, -1, -1)]

    return b.connect(array, size)

def S_transform_reversed(string, N=16, size=8):

    """ V128 -> V128 """

    array = b.split(string, N)
    array = [b.nonlinear_transform_reversed(array[i]) for i in range(N - 1, -1, -1)]
    return b.connect(array, size)

def R_transform(string, N=16, size=8):

    # a0,a1,...,a15
    array = b.split(string, 16, size=8)


    # a15,a14,...,a0
    reversed_array = [array[i] for i in range(N -1, -1, -1)]


    # l(a15||a14||...||a0) -> V(8)
    new_string = b.linear_transform(reversed_array)

    # (l(a15||a14||...||a0) -> V(8)) || (a15||...||a1 -> V(120)) -> V(128)
    result = b.connect([new_string] + reversed_array[:-1], size) # a15||...||a1


    return result

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
    return (b.xor(L_transform(S_transform(X_transform(v128_1, key=key))), v128_0), v128_1)

def LSX_transform(string_128, key):
    return L_transform(S_transform(X_transform(string_128, key=key)))

def LSX_transform_reversed(string_128, key):
    return S_transform_reversed(L_transform_reversed(X_transform(string_128, key=key)))
