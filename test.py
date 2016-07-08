import unittest
import sys
import os
from steganographysaurus import stegg


class TestStegg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # send stderr to /dev/null
        bit_bucket = open(os.devnull, mode='w');
        # sys.stderr = bit_bucket
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
        for x in payload:
            print(x)

        #https://en.wikipedia.org/wiki/List_of_Unicode_characters

    def test_payload_conversion_unicode(self):
        # https://en.wikipedia.org/wiki/List_of_Unicode_characters
        payload = stegg._convert_payload("Ω")
        print(payload)
        for x in payload:
            print(x)

        self.assertEquals(payload.decode(), "Ω")


    def test_non_existing_channel(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(stegg.Barf) as context_manager:
            stegg.hide("eggs", "/dev/bogus")
        self.assertEqual(context_manager.exception.code, 3)

    def test_invalid_channel(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(stegg.Barf) as context_manager:
            stegg.hide("eggs", "/bin/bash")
        self.assertEqual(context_manager.exception.code, 6)

    def test_valid_channel(self):
        # todo: hide message in final image
        stegg.hide("eggs", "./assets/monalisa.jpg")
