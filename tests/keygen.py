#!/usr/bin/env python3

import unittest

import sys # added!
sys.path.append("..")

from hardcoded import nonlinear_coeffs
import keygen as k
import transforms as t


K = 0x8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef
K1 = 0x8899aabbccddeeff0011223344556677
K2 = 0xfedcba98765432100123456789abcdef
K3 = 0xdb31485315694343228d6aef8cc78c44
K4 = 0x3d4553d8e9cfec6815ebadc40a9ffd04
K5 = 0x57646468c44a5e28d3e59246f429f1ac
K6 = 0xbd079435165c6432b532e82834da581b
K7 = 0x51e640757e8745de705727265a0098b1
K8 = 0x5a7925017b9fdd3ed72a91a22286f984
K9 = 0xbb44e25378c73123a5f32f73cdb6e517
K10 =0x72e9dd7416bcf45b755dbaa88e4a4043

C1 = 0x6ea276726c487ab85d27bd10dd849401
C2 = 0xdc87ece4d890f4b3ba4eb92079cbeb02
C3 = 0xb2259a96b4d88e0be7690430a44f7f03
C4 = 0x7bcd1b0b73e32ba5b79cb140f2551504
C5 = 0x156f6d791fab511deabb0c502fd18105
C6 = 0xa74af7efab73df160dd208608b9efe06
C7 = 0xc9e8819dc73ba5ae50f5b570561a6a07
C8 = 0xf6593616e6055689adfba18027aa2a08




class Test(unittest.TestCase):
    def test_split_key(self):
        K1 = 0x8899aabbccddeeff0011223344556677
        K2 = 0xfedcba98765432100123456789abcdef

        result = k.split_key(K)

        self.assertEqual((K1, K2), result)

    def test_generate_constans(self):
        expected = [0x6ea276726c487ab85d27bd10dd849401,
                     0xdc87ece4d890f4b3ba4eb92079cbeb02,
                     0xb2259a96b4d88e0be7690430a44f7f03,
                     0x7bcd1b0b73e32ba5b79cb140f2551504,
                     0x156f6d791fab511deabb0c502fd18105,
                     0xa74af7efab73df160dd208608b9efe06,
                     0xc9e8819dc73ba5ae50f5b570561a6a07,
                     0xf6593616e6055689adfba18027aa2a08,

                     ]
        got = k.generate_constants()[:8]

        self.assertEqual(expected, got)

    def test_iterative_key_generation(self):
        constans = k.generate_constants();

        got = k.iterative_key_generation(K, constans)

        expected = [
            0x8899aabbccddeeff0011223344556677,
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

        self.assertEqual(expected, got)


    def test_X_SX_LSDX(self):
        XC1K1 = t.X_transform(C1, K1), 0xe63bdcc9a09594475d369f2399d1f276,
        SXC1K1 = t.S_transform(t.X_transform(C1, K1)), 0x0998ca37a7947aabb78f4a5ae81b748a
        LSXC1K1 = t.LSX_transform(C1, K1), 0x3d0940999db75d6a9257071d5e6144a6
        FC1K1K2 = t.F_transform((K1, K2), C1), (0xc3d5fa01ebe36f7a9374427ad7ca8949, 0x8899aabbccddeeff0011223344556677)
        FC2FC1K1K2 = t.F_transform(t.F_transform((K1, K2), C1), C2), (0x37777748e56453377d5e262d90903f87, 0xc3d5fa01ebe36f7a9374427ad7ca8949)
        F1_3 = t.F_transform(FC2FC1K1K2[0], C3), (0xf9eae5f29b2815e31f11ac5d9c29fb01, 0x37777748e56453377d5e262d90903f87)
        F1_4 = t.F_transform(F1_3[0], C4), (0xe980089683d00d4be37dd3434699b98f, 0xf9eae5f29b2815e31f11ac5d9c29fb01)
        F1_5 = t.F_transform(F1_4[0], C5), (0xb7bd70acea4460714f4ebe13835cf004, 0xe980089683d00d4be37dd3434699b98f)
        F1_6 = t.F_transform(F1_5[0], C6), (0x1a46ea1cf6ccd236467287df93fdf974, 0xb7bd70acea4460714f4ebe13835cf004)
        F1_7 = t.F_transform(F1_6[0], C7), (0x3d4553d8e9cfec6815ebadc40a9ffd04, 0x1a46ea1cf6ccd236467287df93fdf974)
        F1_8 = t.F_transform(F1_7[0], C8), (0xdb31485315694343228d6aef8cc78c44, 0x3d4553d8e9cfec6815ebadc40a9ffd04)

        self.assertEqual(*XC1K1)
        self.assertEqual(*SXC1K1)
        self.assertEqual(*LSXC1K1)
        self.assertEqual(*FC1K1K2)
        self.assertEqual(*F1_3)
        self.assertEqual(*F1_4)
        self.assertEqual(*F1_5)
        self.assertEqual(*F1_6)
        self.assertEqual(*F1_7)
        self.assertEqual(*F1_8)






# keygen tests

"""
#K1 = 0x8899aabbccddeeff0011223344556677,
#K2 = 0xfedcba98765432100123456789abcdef.
X[C1](K1) = 0xe63bdcc9a09594475d369f2399d1f276,
SX[C1](K1) = 0x0998ca37a7947aabb78f4a5ae81b748a,
LSX[C1](K1) = 0x3d0940999db75d6a9257071d5e6144a6,
F [C1](K1, K2) =  (0xc3d5fa01ebe36f7a9374427ad7ca8949, 0x8899aabbccddeeff0011223344556677)
F [C2]F [C1](K1, K2) =   (0x37777748e56453377d5e262d90903f87, c3d5fa01ebe36f7a9374427ad7ca8949)
F [C3]F[C2]F [C1](K1, K2) = (0xf9eae5f29b2815e31f11ac5d9c29fb01, 0x37777748e56453377d5e262d90903f87).
F [C4]...F [C1](K1, K2) =  (e980089683d00d4be37dd3434699b98f, f9eae5f29b2815e31f11ac5d9c29fb01).
F [C5]xF [C1](K1, K2) = (0xb7bd70acea4460714f4ebe13835cf004, 0xe980089683d00d4be37dd3434699b98f).
F [C6]…F [C1](K1, K2) =   = (0x1a46ea1cf6ccd236467287df93fdf974, 0xb7bd70acea4460714f4ebe13835cf004).
F [C7]…F [C1](K1, K2) =   = (0x3d4553d8e9cfec6815ebadc40a9ffd04, 0x1a46ea1cf6ccd236467287df93fdf974).
(K3, K4) = F [C8]…F [C1](K1, K2) = (0xdb31485315694343228d6aef8cc78c44, 0x3d4553d8e9cfec6815ebadc40a9ffd04).

K1 = 0x8899aabbccddeeff0011223344556677,
K2 = 0xfedcba98765432100123456789abcdef,
K3 = 0xdb31485315694343228d6aef8cc78c44,
K4 = 0x3d4553d8e9cfec6815ebadc40a9ffd04,
K5 = 0x57646468c44a5e28d3e59246f429f1ac,
K6 = 0xbd079435165c6432b532e82834da581b,
K7 = 0x51e640757e8745de705727265a0098b1,
K8 = 0x5a7925017b9fdd3ed72a91a22286f984,
K9 = 0xbb44e25378c73123a5f32f73cdb6e517,
K10= 0x72e9dd7416bcf45b755dbaa88e4a4043.

b = 7f679d90bebc24305a468d42b9d4edcd,
X[K10](b) = 0d8e40e4a800d06b2f1b37ea379ead8e,
-1X[K10](b) = 8a6b930a52211b45c5baa43ff8b91319,
S-1L-1X[K10](b) = 76ca149eef27d1b10d17e3d5d68e5a72,
S-1L-1X[K9]S-1L-1X[K10](b) = 5d9b06d41b9d1d2d04df7755363e94a9,
S-1L-1X[K8]…S-1L-1X[K10](b) = 79487192aa45709c115559d6e9280f6e,
S-1L-1X[K7]…kS-1L-1X[K10](b) = ae506924c8ce331bb918fc5bdfb195fa,
S-1L-1X[K6]…S-1L-1X[K10](b) = bbffbfc8939eaaffafb8e22769e323aa,
S-1L-1X[K5]…S-1L-1X[K10](b) = 3cc2f07cc07a8bec0f3ea0ed2ae33e4a,
S-1L-1X[K4]…S-1L-1X[K10](b) = f36f01291d0b96d591e228b72d011c36,
S-1L-1X[K3]… S-1L-1X[K10](b) = 1c4b0c1e950182b1ce696af5c0bfc5df,
S-1L-1X[K2]… S-1L-1X[K10](b) = 99bb99ff99bb99ffffffffffffffffff.

a = X[K1]S-1L-1X[K2]…S-1L-1X[K10](b) = 1122334455667700ffeeddccbbaa9988.
"""
