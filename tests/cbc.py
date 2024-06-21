#!/usr/bin/env python3

import unittest

import sys # added!
sys.path.append("..")




import cbc_mode.cbc as cbc
from preprocessing import encode
from keygen import generate_main_key

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
        key = generate_main_key()
        print("TESTING ENCRYPTION:")
        print(cbc.encrypt(TEXT, key))
        print("ГЫГЫГ :")
        self.assertEqual(cbc.decrypt(cbc.encrypt(TEXT, key), key), TEXT)
        self.assertEqual(cbc.decrypt(cbc.encrypt(TEXT1, key), key), TEXT1)
        self.assertEqual(cbc.decrypt(cbc.encrypt(TEXT2, key), key), TEXT2)
