#!/usr/bin/env python3

import unittest

import sys # added!
sys.path.append("..")




import cbc_mode.cbc as cbc
from preprocessing import encode

TEXT = encode("IIt’s up to brave hearts, sir, to be patient when things are going badly, as well as being happy when they\'re going well.It’s up to brave hearts, sir, to be patient when things are going badly, as well as being happy when they\'re going well.It’s up to brave hearts, sir, to be patient when things are going badly, as well as being happy when they\'re going well.t’s up to brave hearts, sir, to be patient when things are going badly, as well as being happy when they\'re going well.")
TEXT1 = encode("")
TEXT2 = encode(" ")

class Test(unittest.TestCase):
    def test_split(self):
        blocks = cbc.split_to_blocks(TEXT)
        text = cbc.unir(blocks)
        #for i in range(len(blocks)):
        #    text += blocks[i] << 128*i

        self.assertEqual(text, TEXT)
    def test_encrypt(self):
        ID = lambda text,key: text
        self.assertEqual(cbc.decrypt(cbc.encrypt(TEXT, 0, ID), 0, ID ), TEXT)
        self.assertEqual(cbc.decrypt(cbc.encrypt(TEXT1, 0, ID), 0, ID ), TEXT1)
        self.assertEqual(cbc.decrypt(cbc.encrypt(TEXT2, 0, ID), 0, ID ), TEXT2)
