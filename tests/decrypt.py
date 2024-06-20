
#!/usr/bin/env python3
import unittest

import sys # added!
sys.path.append("..")

from hardcoded import nonlinear_coeffs
from basic import compose_n_times
import keygen as k
import transforms as t
from cypher import decrypt


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


b = 0x7f679d90bebc24305a468d42b9d4edcd
XK10 = 0x0d8e40e4a800d06b2f1b37ea379ead8e

LrX_K10= 0x8a6b930a52211b45c5baa43ff8b91319


LSXrs = [0x76ca149eef27d1b10d17e3d5d68e5a72,
0x5d9b06d41b9d1d2d04df7755363e94a9,
0x79487192aa45709c115559d6e9280f6e,
0xae506924c8ce331bb918fc5bdfb195fa,
0xbbffbfc8939eaaffafb8e22769e323aa,
0x3cc2f07cc07a8bec0f3ea0ed2ae33e4a,
0xf36f01291d0b96d591e228b72d011c36,
0x1c4b0c1e950182b1ce696af5c0bfc5df,
0x99bb99ff99bb99ffffffffffffffffff,]



from transforms import X_transform as X, S_transform as S, LSX_transform_reversed as LSXr, L_transform_reversed as Lr

a = 0x1122334455667700ffeeddccbbaa9988

class Test(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(X(b, Ks[9]), XK10)
        self.assertEqual(Lr(X(b, Ks[9])), LrX_K10)
        step = b
        for i in range(9, 0, -1):
            step = LSXr(step, Ks[i])
            self.assertEqual(step, LSXrs[9 - i])
        self.assertEqual(X(step,Ks[0]), a)
        self.assertEqual(decrypt(b, K),a)
