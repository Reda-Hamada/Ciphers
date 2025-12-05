from crypto.BaseCipher import BaseCipher
import random

class OneTimePad(BaseCipher):

    def __init__(self, key=None):
        self.key = key  

    def prepare_key(self, length=None):
        """Generate random key if self.key is None."""
        if not self.key:
            self.key = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(length))
        return self.key

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        # generate key if not present
        self.prepare_key(length=len(plaintext))
        cipher = ""
        for p, k in zip(plaintext, self.key):
            c = (self.char_to_int(p) + self.char_to_int(k)) % 26
            cipher += self.int_to_char(c)
        return cipher

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)
        if not self.key:
            raise ValueError("Key is required for decryption!")
        plain = ""
        for c, k in zip(ciphertext, self.key):
            p = (self.char_to_int(c) - self.char_to_int(k)) % 26
            plain += self.int_to_char(p)
        return plain
