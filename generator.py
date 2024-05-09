#!/usr/bin/env python3


# Generating all kinds of values which could be possible in linear transformation

from hardcoded import nonlinear_coeffs

from basic import string_to_galua

def gen_l_transforms():
    t = [[]]*16
    for i in range(len(nonlinear_coeffs)):
        print("AAAAAAAAAAA \n\n\n")
        t[i] = [0]*256
        for j in range(256):
            a = string_to_galua(j * nonlinear_coeffs[i])
            print(a, j)
            t[i][j] = a
    return t

def gen_GF():
    a = []
    for i in range(256):
        a.append(string_to_galua(i*32))
    return a

a = gen_l_transforms()

m = 0
for i in a:
    print("[ # for ", nonlinear_coeffs[m])
    m+=1
    for j in range(256):
        if j%16 == 0:
            print()
        print(i[j], end=', ')
    print("],")
