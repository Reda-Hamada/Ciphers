import math
import numpy as np

from .BaseCipher import BaseCipher

class HillCipher(BaseCipher):
    def __init__(self, key):
        """
        key is a string have the 4 chars.
        :param key:
        """
        key = self.normalize(key)
        self.length = len(key)
        self.size = int(math.sqrt(self.length))
        if self.size * self.size != self.length:
            raise Exception('Invalid key length')

        self.key = key
        self.key_matrix = self.prepare_key()


    def prepare_key(self):
        matrix = []
        idx = 0
        for i in range(self.size):
            raw = []
            for j in range(self.size):
                raw.append(self.char_to_int(self.key[idx]))
                idx += 1
            matrix.append(raw)

        return np.array(matrix)

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)

        ciphertext = ""
        for i in range(0, len(plaintext), self.size):
            block = np.array([[self.char_to_int(c)] for c in plaintext[i:i+self.size]])
            result = np.dot(self.key_matrix, block) % 26

            for num in result:
                ciphertext += self.int_to_char(num[0])

        return ciphertext

    @staticmethod
    def mod_inverse(a, m):
        a = a % m
        for i in range(m):
            if (a * i) % m == 0:
                return i
        raise Exception('Modular inverse does not exist')

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)

        plaintext = ""

        det = int(round(np.linalg.det(self.key_matrix)))
        det_inv = self.mod_inverse(det, 26)

        adj = np.round(np.linalg.inv(self.key_matrix) * det).astype(int)

        inv_matrix = (det_inv * adj) % 26

        for i in range(0, len(ciphertext), self.size):
            block = np.array([[self.char_to_int(c)] for c in ciphertext[i:i+self.size]])
            result = np.dot(inv_matrix, block) % 26

            for num in result:
                plaintext += self.int_to_char(num[0])

        return plaintext

