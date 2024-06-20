#!/usr/bin/env python3
import unittest

import sys # added!
sys.path.append("..")

from hardcoded import nonlinear_coeffs
from basic import compose_n_times
import keygen as k
import transforms as t
from cypher import encrypt


K = 0x8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef
Ks = [0x8899aabbccddeeff0011223344556677,
0xfedcba98765432100123456789abcdef,
0xdb31485315694343228d6aef8cc78c44,
0x3d4553d8e9cfec6815ebadc40a9ffd04,
0x57646468c44a5e28d3e59246f429f1ac,
0xbd079435165c6432b532e82834da581b,
0x51e640757e8745de705727265a0098b1,
0x5a7925017b9fdd3ed72a91a22286f984,
0xbb44e25378c73123a5f32f73cdb6e517,
0x72e9dd7416bcf45b755dbaa88e4a4043,
]

C1 = 0x6ea276726c487ab85d27bd10dd849401
C2 = 0xdc87ece4d890f4b3ba4eb92079cbeb02
C3 = 0xb2259a96b4d88e0be7690430a44f7f03
C4 = 0x7bcd1b0b73e32ba5b79cb140f2551504
C5 = 0x156f6d791fab511deabb0c502fd18105
C6 = 0xa74af7efab73df160dd208608b9efe06
C7 = 0xc9e8819dc73ba5ae50f5b570561a6a07
C8 = 0xf6593616e6055689adfba18027aa2a08



X_K1           =0x99bb99ff99bb99ffffffffffffffffff
SX_K1          =0xe87de8b6e87de8b6b6b6b6b6b6b6b6b6
LSXs = [0xe297b686e355b0a1cf4a2f9249140830,
       0x285e497a0862d596b36f4258a1c69072,
       0x0187a3a429b567841ad50d29207cc34e,
       0xec9bdba057d4f4d77c5d70619dcad206,
       0x1357fd11de9257290c2a1473eb6bcde1,
       0x28ae31e7d4c2354261027ef0b32897df,
       0x07e223d56002c013d3f5e6f714b86d2d,
       0xcd8ef6cd97e0e092a8e4cca61b38bf65,
       0x0d8e40e4a800d06b2f1b37ea379ead8e,
       ]
b = 0x7f679d90bebc24305a468d42b9d4edcd


from transforms import X_transform as X, S_transform as S, LSX_transform as LSX

a = 0x1122334455667700ffeeddccbbaa9988

class Test(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(X(a, Ks[0]), X_K1)
        self.assertEqual(S(X(a, Ks[0])), SX_K1)
        step = a
        for i in range(0, 9):
            step = LSX(step, Ks[i])
            self.assertEqual(step, LSXs[i])
        self.assertEqual(b, X(step, Ks[9]))
        self.assertEqual(b, encrypt(a, K))
