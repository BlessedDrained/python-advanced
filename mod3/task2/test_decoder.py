from application.mod2.task3 import decrypt
import unittest

class DecoderTest(unittest.TestCase):
    def test_check_decoder_1_dot_1(self):
        expected = 'абра-кадабра'
        actual = decrypt('абра-кадабра.')
        self.assertEqual(expected, actual)

    def test_check_decoder_1_dot_2(self):
        expected = ''
        actual = decrypt('.')
        self.assertEqual(expected, actual)

    def test_check_decoder_2_dots_1(self):
        expected = 'абра-кадабра'
        actual = decrypt('абраа..-кадабра')
        self.assertEqual(expected, actual)

    def test_check_decoder_2_dots_2(self):
        expected = 'абра-кадабра'
        actual = decrypt('абра--..кадабра')
        self.assertEqual(expected, actual)

    def test_check_decoder_3_dots_1(self):
        expected = 'абра-кадабра'
        actual = decrypt('абраа..-.кадабра')
        self.assertEqual(expected, actual)

    def test_check_decoder_3_dots_2(self):
        expected = 'абра-кадабра'
        actual = decrypt('абрау...-кадабра')
        self.assertEqual(expected, actual)

    def test_check_decoder_3_dots_3(self):
        expected = '23'
        actual = decrypt('1..2.3')
        self.assertEqual(expected, actual)

    def test_check_decoder_more_than_3_dots_1(self):
        expected = ''
        actual = decrypt('абра........')
        self.assertEqual(expected, actual)

    def test_check_decoder_more_than_3_dots_2(self):
        expected = 'a'
        actual = decrypt('абр......a.')
        self.assertEqual(expected, actual)

    def test_check_decoder_more_than_3_dots_3(self):
        expected = ''
        actual = decrypt('1.......................')
        self.assertEqual(expected, actual)