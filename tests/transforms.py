#!/usr/bin/env python3

import unittest

import sys # added!
sys.path.append("..")

import transforms as tr
import random


class Test(unittest.TestCase):
    def test_R_transform(self):
       """
       Example from GOST
       А.1.2 Преобразование R
       R(00000000000000000000000000000100) = 0x94000000000000000000000000000001,
       R(94000000000000000000000000000001) = 0xa5940000000000000000000000000000,
       R(a5940000000000000000000000000000) = 0x64а59400000000000000000000000000,
       R(64a59400000000000000000000000000) = 0x0d64a594000000000000000000000000.
       """

       self.assertEqual(tr.R_transform(0x00000000000000000000000000000100),0x94000000000000000000000000000001)
       self.assertEqual(tr.R_transform(0x94000000000000000000000000000001),0xa5940000000000000000000000000000)
       self.assertEqual(tr.R_transform(0xa5940000000000000000000000000000),0x64a59400000000000000000000000000)
       self.assertEqual(tr.R_transform(0x64a59400000000000000000000000000),0x0d64a594000000000000000000000000)


       got = random.randint(0, 2**128)
       expected = tr.R_transform_reversed(tr.R_transform(got))
       self.assertEqual(got, expected)

    def test_S_transform(self):

        expected = [
            0xb66cd8887d38e8d77765aeea0c9a7efc,
            0x559d8dd7bd06cbfe7e7b262523280d39,
            0x0c3322fed531e4630d80ef5c5a81c50b,
            0x23ae65633f842d29c5df529c13f5acda
        ]

        got = [
            tr.S_transform(0xffeeddccbbaa99881122334455667700),
            tr.S_transform(0xb66cd8887d38e8d77765aeea0c9a7efc),
            tr.S_transform(0x559d8dd7bd06cbfe7e7b262523280d39),
            tr.S_transform(0x0c3322fed531e4630d80ef5c5a81c50b),
        ]

        self.assertEqual(expected, got)

    def test_S_transform_reversed(self):

        expected = [
            0xffeeddccbbaa99881122334455667700,
            0xb66cd8887d38e8d77765aeea0c9a7efc,
            0x559d8dd7bd06cbfe7e7b262523280d39,
            0x0c3322fed531e4630d80ef5c5a81c50b
        ]

        got = [
            tr.S_transform_reversed(0xb66cd8887d38e8d77765aeea0c9a7efc),
            tr.S_transform_reversed(0x559d8dd7bd06cbfe7e7b262523280d39),
            tr.S_transform_reversed(0x0c3322fed531e4630d80ef5c5a81c50b),
            tr.S_transform_reversed(0x23ae65633f842d29c5df529c13f5acda),
        ]

        self.assertEqual(expected, got)

    def test_L_transform(self):

        got = [
            tr.L_transform(0x64a59400000000000000000000000000),
            tr.L_transform(0xd456584dd0e3e84cc3166e4b7fa2890d),
            tr.L_transform(0x79d26221b87b584cd42fbc4ffea5de9a),
            tr.L_transform(0x0e93691a0cfc60408b7b68f66b513c13),
        ]

        expected = [
            0xd456584dd0e3e84cc3166e4b7fa2890d,
            0x79d26221b87b584cd42fbc4ffea5de9a,
            0x0e93691a0cfc60408b7b68f66b513c13,
            0xe6a8094fee0aa204fd97bcb0b44b8580,
        ]

        self.assertEqual(expected, got)




    def test_L_transform_reversed(self):
        got = [
         tr.L_transform_reversed(0xd456584dd0e3e84cc3166e4b7fa2890d),
         tr.L_transform_reversed(0x79d26221b87b584cd42fbc4ffea5de9a),
         tr.L_transform_reversed(0x0e93691a0cfc60408b7b68f66b513c13),
         tr.L_transform_reversed(0xe6a8094fee0aa204fd97bcb0b44b8580),
     ]

        expected = [
         0x64a59400000000000000000000000000,
         0xd456584dd0e3e84cc3166e4b7fa2890d,
         0x79d26221b87b584cd42fbc4ffea5de9a,
         0x0e93691a0cfc60408b7b68f66b513c13,
     ]

        self.assertEqual(expected, got)
