import math
import numpy as np
from .BaseCipher import BaseCipher


class HillCipher(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.key_matrix = None
        self.size = None
        self.length = None
        self.prepare_key()

    def prepare_key(self):
        """Convert key string to matrix"""
        key = self.normalize(self.key)
        self.length = len(key)
        self.size = int(math.sqrt(self.length))

        if self.size * self.size != self.length:
            raise ValueError('Invalid key length - must be perfect square')

        matrix = []
        idx = 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.char_to_int(key[idx]))
                idx += 1
            matrix.append(row)

        self.key_matrix = np.array(matrix)
        return self.key_matrix

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)

        # Pad if needed
        while len(plaintext) % self.size != 0:
            plaintext += 'X'

        ciphertext = ""
        for i in range(0, len(plaintext), self.size):
            block = np.array([[self.char_to_int(c)] for c in plaintext[i:i + self.size]])
            result = np.dot(self.key_matrix, block) % 26
            for num in result:
                ciphertext += self.int_to_char(num[0])

        return ciphertext

    @staticmethod
    def mod_inverse(a, m):
        """Find modular multiplicative inverse"""
        a = a % m
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError('Modular inverse does not exist')

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)

        det = int(round(np.linalg.det(self.key_matrix))) % 26
        det_inv = self.mod_inverse(det, 26)

        adj = np.round(np.linalg.inv(self.key_matrix) * det).astype(int)
        inv_matrix = (det_inv * adj) % 26

        plaintext = ""
        for i in range(0, len(ciphertext), self.size):
            block = np.array([[self.char_to_int(c)] for c in ciphertext[i:i + self.size]])
            result = np.dot(inv_matrix, block) % 26
            for num in result:
                plaintext += self.int_to_char(num[0])

        return plaintext

