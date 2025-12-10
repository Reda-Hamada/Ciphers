from .BaseCipher import BaseCipher  # or absolute import



class Caesar(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.prepare_key()

    def prepare_key(self):
        """Validate key is an integer"""
        if not isinstance(self.key, int):
            raise ValueError("Caesar key must be an integer")
        return self.key

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        ciphertext = ""
        for char in plaintext:
            ciphertext += self.int_to_char(self.char_to_int(char) + self.key)
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)
        plaintext = ""
        for char in ciphertext:
            plaintext += self.int_to_char(self.char_to_int(char) - self.key)
        return plaintext
