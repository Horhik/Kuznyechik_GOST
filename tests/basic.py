#!/usr/bin/env python3

import unittest

import sys # added!
sys.path.append("..")

import basic


class Test(unittest.TestCase):

    def test_xor(self):
        a = 0b101011
        b = 0b111000
        expected = a^b
        result = basic.xor(a, b)
        self.assertEqual(expected, result)

    def test_split(self):
        ai, al, ar = (0b101010, 3, [0b10, 0b10, 0b10] )
        bi, bl, br = (0b01010,  3, [0b10 , 0b10, 0b0] )
        ci, cl, cr = (0b1,      3, [0b1 , 0b0 , 0b0 ] )
        self.assertEqual([basic.split(ai, al), basic.split(bi, bl), basic.split(ci, cl)],
                         [ar,br,cr])

    def test_ring_to_string(self):
        self.assertEqual(True, True)

    def test_string_to_ring(self):
        pass

    def test_string_to_galua(self):
        """
        V8 -> GF(2)[x]/p(x)
        Example:

        INPUT:
        q(x) = x11 + x9 + x8 + x7 + x6 + x3 + x + 1
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

        self.assertEqual(154, basic.string_to_galua(3019))


    def test_galua_to_string(self):
        pass

    def test_compose_n_times(self):
        pass

    def test_linear_transform(self):
        pass

    def test_nonlinear_transform(self):
        pass

    def test_nonlinear_transform_reversed(self):
        pass



if __name__ == '__main__':
    unittest.main()
