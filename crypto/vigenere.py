from .BaseCipher import BaseCipher


class Vigenere(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.prepared_key = None
        self.prepare_key()

    def prepare_key(self):
        """Normalize key"""
        self.prepared_key = self.normalize(self.key)
        if len(self.prepared_key) == 0:
            raise ValueError("Key cannot be empty")
        return self.prepared_key

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            p = self.char_to_int(char)
            shift = self.char_to_int(self.prepared_key[key_index % len(self.prepared_key)])
            c = self.int_to_char(p + shift)
            ciphertext += c
            key_index += 1

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)
        plaintext = ""
        key_index = 0

        for char in ciphertext:
            c = self.char_to_int(char)
            shift = self.char_to_int(self.prepared_key[key_index % len(self.prepared_key)])
            p = self.int_to_char(c - shift)
            plaintext += p
            key_index += 1

        return plaintext


    