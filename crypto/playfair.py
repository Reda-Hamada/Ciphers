import string

from .BaseCipher import BaseCipher

import string


class PlayfairCipher(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.matrix = None
        self.prepare_key()

    def prepare_key(self):
        """Create 5x5 matrix from key"""
        key = self.key.lower().replace(" ", "").replace("j", "i")
        matrix = []
        unique = set()

        for char in key:
            if char not in unique and char in string.ascii_lowercase:
                matrix.append(char)
                unique.add(char)

        for char in string.ascii_lowercase:
            if char == 'j':
                continue
            if char not in unique:
                matrix.append(char)
                unique.add(char)

        self.matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
        return self.matrix

    def normalize(self, text):
        """Override to handle Playfair-specific normalization"""
        return text.replace(" ", "").lower().replace("j", "i")

    def divide_plaintext(self, text):
        """Divide text into digraphs"""
        text = self.normalize(text)
        plaintext = ""
        i = 0

        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else "x"

            if a == b:
                plaintext += a + "x"
                i += 1
            else:
                plaintext += a + b
                i += 2

        if len(plaintext) % 2 != 0:
            plaintext += "x"

        return plaintext

    def find_position(self, char):
        """Find row and column of character in matrix"""
        for r in range(5):
            for c in range(5):
                if self.matrix[r][c] == char:
                    return r, c
        return None

    def encrypt(self, plaintext):
        plaintext = self.divide_plaintext(plaintext)
        ciphertext = ""

        for i in range(0, len(plaintext), 2):
            a, b = plaintext[i], plaintext[i + 1]
            r1, c1 = self.find_position(a)
            r2, c2 = self.find_position(b)

            if r1 == r2:
                ciphertext += self.matrix[r1][(c1 + 1) % 5]
                ciphertext += self.matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                ciphertext += self.matrix[(r1 + 1) % 5][c1]
                ciphertext += self.matrix[(r2 + 1) % 5][c2]
            else:
                ciphertext += self.matrix[r1][c2]
                ciphertext += self.matrix[r2][c1]

        return ciphertext.upper()

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.lower()
        plaintext = ""

        for i in range(0, len(ciphertext), 2):
            a, b = ciphertext[i], ciphertext[i + 1]
            r1, c1 = self.find_position(a)
            r2, c2 = self.find_position(b)

            if r1 == r2:
                plaintext += self.matrix[r1][(c1 - 1) % 5]
                plaintext += self.matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                plaintext += self.matrix[(r1 - 1) % 5][c1]
                plaintext += self.matrix[(r2 - 1) % 5][c2]
            else:
                plaintext += self.matrix[r1][c2]
                plaintext += self.matrix[r2][c1]

        return plaintext.upper()
