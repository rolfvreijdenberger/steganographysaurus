import unittest
import sys
import os
from steganographosaurus import stegg


class TestStegg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # send stderr to /dev/null
        bit_bucket = open(os.devnull, mode='w');
        sys.stderr = bit_bucket
        # sys.stdout = bit_bucket
        pass

    @classmethod
    def tearDownClass(cls):
        # restore stderr
        sys.stderr = sys.__stderr__
        # sys.stdout = sys.__stdout__

    def test_payload_conversion(self):
        payload = stegg._convert_payload("ham")
        self.assertEquals(payload.decode(), "ham")
        self.assertEquals(payload, b'ham')
        a = bytearray(b'ham')
        print(bin(a[0])[2:].zfill(8))


    def test_non_existing_carrier(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(SystemExit) as context_manager:
            stegg.hide("eggs", "/dev/bogus")
        self.assertEqual(context_manager.exception.code, 3)

    def test_invalid_carrier(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(SystemExit) as context_manager:
            stegg.hide("eggs", "/bin/bash")
        self.assertEqual(context_manager.exception.code, 1)
