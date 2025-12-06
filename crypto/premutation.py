from .BaseCipher import BaseCipher


class RowTranspositionCipher(BaseCipher):
    def _normalize_key(self, key):
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

    def encrypt(self, plaintext, key, pad_char='X'):
        self._original_text = plaintext
        text_upper = self._original_text.replace(" ", "").upper()


        key_order = self._normalize_key(key)
        cols = len(key_order)

        if len(text_upper) % cols != 0:
            text_upper += pad_char * (cols - (len(text_upper) % cols))

        rows = [text_upper[i:i + cols] for i in range(0, len(text_upper), cols)]

        ciphertext = ""
        for col in key_order:
            for row in rows:
                ciphertext += row[col]

        return ciphertext

    def decrypt(self, ciphertext, key, pad_char='X'):
        key_order = self._normalize_key(key)
        cols = len(key_order)
        rows_count = len(ciphertext) // cols

        matrix = [[""] * cols for _ in range(rows_count)]

        index = 0
        for col in key_order:
            for row in range(rows_count):
                matrix[row][col] = ciphertext[index]
                index += 1

        plaintext_upper = "".join("".join(row) for row in matrix).rstrip(pad_char)
        return self._original_text
