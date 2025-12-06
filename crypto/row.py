from .BaseCipher import BaseCipher
import random

class RowTransposition(BaseCipher):

    def __init__(self, key=None, cols=5):
        self.key = None
        self.cols = cols
        self.prepare_key(key)

    def prepare_key(self, key=None):
        """Prepare numeric key (e.g., 3 1 2). If no key → random permutation."""
        if key:
            self.key = [int(x) for x in key.split()]
        else:
            self.key = list(range(1, self.cols + 1))
            random.shuffle(self.key)
        return self.key

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        cols = len(self.key)
        rows = (len(plaintext) + cols - 1) // cols
        padded = plaintext.ljust(rows * cols, "X")
        table = [list(padded[i:i+cols]) for i in range(0, len(padded), cols)]

        cipher = ""
        for col_num in sorted(self.key):
            col_index = self.key.index(col_num)
            for r in range(rows):
                cipher += table[r][col_index]

        return cipher

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)
        cols = len(self.key)
        rows = len(ciphertext) // cols

        sorted_key = sorted(self.key)
        col_lengths = rows
        columns = {}
        idx = 0
        for col_num in sorted_key:
            columns[col_num] = ciphertext[idx:idx + col_lengths]
            idx += col_lengths

        table = []
        for r in range(rows):
            row = []
            for num in self.key:
                row.append(columns[num][r])
            table.append(row)

        plain = "".join("".join(row) for row in table)
        return plain.rstrip("X")
