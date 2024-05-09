#!/usr/bin/env python3

import numpy as np

from hardcoded import l

S = [ 252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233,
      119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101,
      90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143,
      160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42,
      104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156,
      183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178,
      177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223,
      245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236,
      222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0,
      98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163,
      165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136,
      217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133,
      97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
      116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182]

# S block reversed
Sr =[ 165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145,
      100, 3, 87, 90, 28, 96, 7, 24, 33, 114, 168, 209, 41, 198, 164, 63,
      224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229, 66, 228, 21, 183,
      200, 6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213,
      195, 175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47,
      155, 67, 239, 217, 121, 182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30,
      162, 223, 166, 254, 172, 34, 249, 226, 74, 188, 53, 202, 238, 120, 5, 107,
      81, 225, 89, 163, 242, 113, 86, 17, 106, 137, 148, 101, 140, 187, 119, 60,
      123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54,
      219, 105, 179, 20, 149, 190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173,
      55, 97, 75, 185, 227, 186, 241, 160, 133, 131, 218, 71, 197, 176, 51, 250,
      150, 111, 110, 194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125, 236, 88,
      247, 31, 251, 124, 9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4,
      235, 248, 243, 62, 61, 189, 138, 136, 221, 205, 11, 19, 152, 2, 147, 128,
      144, 208, 36, 52, 203, 237, 244, 206, 153, 16, 68, 64, 146, 58, 1, 38,
      18, 26, 72, 104, 245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116]

""" Base functions """


def split(block, parts):

    """
    V(n) -> [V(n/number)]
    Splitting V to `number` parts
    """
    bits = []
    size = int(np.ceil(block.bit_length() / parts))

    for i in range(parts):
        """
        example
        # 1011 -> 10
        # 10 -> 1000
        # 1000 xor 1011 -> 0011 -> 11
        """
        shifted = block >> size
        bits.append((shifted << size)^block)
        block = shifted
    return np.array(bits)



def xor(A, B):

    """ Vs -> Vs """

    return A ^ B


def ring_to_string(ring, size=8):

    """ Z2^s -> Vs """


    return ring

def string_to_ring(string, size=8):

    """ Vs -> Z2^s """

    return string % 2**size

def string_to_galua(string, size=8):

    """
        V8 -> GF(2)[x]/p(x)
        Definitions:
        Converting one-byte-string (8bit integer)
        into element of finite field over Z2 by polynom p(x)

        x^k = xk
        Example:

        INPUT:
        q(x) = x11 + x9 + x8 + x7 + x6 + x3 + x + 1

        or as array
         0  1  2  3  4  5  6  7  8  9  10 11
         |  |  |  |  |  |  |  |  |  |  |  |
        [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1] # reversed order

        or as number
        0b101111001011 == 3019


        p(x) = x8 + x7 + x6 + x + 1

        RESULT:
        q(x)/p(x) = r(x)

        p(x)*m(x) + r(x) = q(x)

        m(x) = x3 + x2 + x + 1
        r(x) = x7 + x4 + x3 + x

        int(r(x)) = 0b10011010 = 154

        154 <- returned value

     """



    # Turning int into array of bits in reversed order
    polynom = np.array([int(x) for x in bin(string)[2:]])
    # p(x) = x^8 + x^7 + x^6 + x + 1
    px = np.array([1, 1, 1, 0, 0, 0, 0, 1, 1])

    # dividing polynomials (indexes of both in reversed order)
    result = np.polydiv(polynom, px)[1]%2

    # Finding the highest power of resulted polynomial
    P = len(result) - 1 # hightest power

    # Reversing the order to be as it is
    # Turing into int from binary representation
    result = sum([result[i]*2**(P - i) for i in range(P, -1, -1)])

    return int(result)



def galua_to_string(galua):
    return int(''.join(str(i) for i in galua), 2)


def compose_n_times(function, argument, times, times_change=lambda x: x -1):
    if times == 1:
        return function(argument)
    else:
        return function(compose_n_times(function, argument, times_change(times)))

def linear_transform(string_array):
    """
    Transforming data of 16 bytes by linear transform defined by
    xoring (summing over Z/2 ) precalculated values of operations over galious field
    by irreducable polynomial x^8 + x^7 + x^6 + x + 1

   linear transform.
    |
    |               this operation is uneccesarry due to xoring 8bit values
    |               will not exceed 8bit
    ↓               |
    ℓ(a15, …, a0) = ↓
                    ∇(148 ∙ ∆(a15) +
                       32 ∙ ∆(a14) +
                      133 ∙ ∆(a13) +
                       16 ∙ ∆(a12) +
                      194 ∙ ∆(a11) +
                      192 ∙ ∆(a10) +
                        1 ∙ ∆(a9) +
                      251 ∙ ∆(a8) +
                        1 ∙ ∆(a7) +
                      192 ∙ ∆(a6) +
                      194 ∙ ∆(a5) +
                       16 ∙ ∆(a4) +
                      133 ∙ ∆(a3) +
                       32 ∙ ∆(a2) +
                      148 ∙ ∆(a1) +
                        1 ∙ ∆(a0))

                      all operations here are over F
    """
    result = 0
    # sum values over Z/2
    for i in range(15):
        result ^= l[i][string_array[15 - i]]




def nonlinear_transform(string): #eight bit string
    return ring_to_string(S[string_to_ring(string)], size=8)

def nonlinear_transform_reversed(string): #eight bit string
    return ring_to_string(Sr[string_to_ring(string)], size=8)
