from .BaseCipher import BaseCipher


class rotor(BaseCipher):
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass
