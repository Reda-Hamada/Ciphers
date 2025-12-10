from .BaseCipher import BaseCipher


class RowTranspositionCipher(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.key_order = None
        self._original_text = None
        self.prepare_key()

    def prepare_key(self):
        """Convert key to column order"""
        key_order = self._normalize_key(self.key)
        self.key_order = key_order
        return self.key_order

    def _normalize_key(self, key):
        """Helper method to normalize key format"""
        if isinstance(key, str):
            if " " in key:
                key_list = [int(x) for x in key.split()]
            else:
                key_list = [int(x) for x in key]
        elif isinstance(key, list):
            key_list = key
        else:
            raise ValueError("Invalid key format")

        order = sorted(range(len(key_list)), key=lambda i: key_list[i])
        return order

    def encrypt(self, plaintext, pad_char='X'):
        """Encrypt using row transposition"""
        self._original_text = plaintext
        text_upper = self.normalize(plaintext)

        cols = len(self.key_order)

        # Pad text if needed
        if len(text_upper) % cols != 0:
            text_upper += pad_char * (cols - (len(text_upper) % cols))

        # Create rows
        rows = [text_upper[i:i + cols] for i in range(0, len(text_upper), cols)]

        # Read by column order
        ciphertext = ""
        for col in self.key_order:
            for row in rows:
                ciphertext += row[col]

        return ciphertext

    def decrypt(self, ciphertext, pad_char='X'):
        """Decrypt using row transposition"""
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

        # Return original text if stored, otherwise return decrypted
        if self._original_text:
            return self._original_text
        return plaintext
