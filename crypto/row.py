from .BaseCipher import BaseCipher

class RowTransposition(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.key_order = None
        self.prepare_key()

    def prepare_key(self):
        """Convert key to column order"""
        if isinstance(self.key, str):
            if " " in self.key:
                key_list = [int(x) for x in self.key.split()]
            else:
                key_list = [int(x) for x in self.key]
        elif isinstance(self.key, list):
            key_list = self.key
        else:
            raise ValueError("Invalid key format")

        self.key_order = sorted(range(len(key_list)), key=lambda i: key_list[i])
        return self.key_order

    def encrypt(self, plaintext, pad_char='X'):
        plaintext = self.normalize(plaintext)
        cols = len(self.key_order)

        # Pad text
        if len(plaintext) % cols != 0:
            plaintext += pad_char * (cols - (len(plaintext) % cols))

        # Create rows
        rows = [plaintext[i:i + cols] for i in range(0, len(plaintext), cols)]

        # Read by column order
        ciphertext = ""
        for col in self.key_order:
            for row in rows:
                ciphertext += row[col]

        return ciphertext

    def decrypt(self, ciphertext, pad_char='X'):
        ciphertext = self.normalize(ciphertext)
        cols = len(self.key_order)
        rows_count = len(ciphertext) // cols

        # Create empty matrix
        matrix = [[""] * cols for _ in range(rows_count)]

        # Fill matrix by column order
        index = 0
        for col in self.key_order:
            for row in range(rows_count):
                matrix[row][col] = ciphertext[index]
                index += 1

        # Read row by row
        plaintext = "".join("".join(row) for row in matrix).rstrip(pad_char)
        return plaintext

