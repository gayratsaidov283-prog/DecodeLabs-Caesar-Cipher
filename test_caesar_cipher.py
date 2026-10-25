import unittest
from caesar_cipher import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(
            encrypt("HELLO WORLD!!", 4),
            "LIPPS ASVPH!!"
        )

    def test_decrypt(self):
        self.assertEqual(
            decrypt("LIPPS ASVPH!!", 4),
            "HELLO WORLD!!"
        )

    def test_lowercase(self):
        self.assertEqual(
            encrypt("hello", 3),
            "khoor"
        )

    def test_preserve_symbols(self):
        self.assertEqual(
            encrypt("Hello, World! 123", 3),
            "Khoor, Zruog! 123"
        )

    def test_wraparound(self):
        self.assertEqual(
            encrypt("XYZ xyz", 3),
            "ABC abc"
        )

    def test_round_trip(self):
        original = "Decode Labs Project 2!"
        encrypted = encrypt(original, 7)
        decrypted = decrypt(encrypted, 7)

        self.assertEqual(decrypted, original)


if __name__ == "__main__":
    unittest.main()