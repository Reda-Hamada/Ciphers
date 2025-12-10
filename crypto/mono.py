from .BaseCipher import BaseCipher


class MonoCipher(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.prepared_key = None
        self.decrypt_mapping = None
        self.prepare_key()

    def prepare_key(self):
        """Build 26-letter substitution alphabet from key"""
        key = self.key.upper()
        seen = set()
        final_key = ""

        for ch in key:
            if ch not in seen and ch.isalpha():
                seen.add(ch)
                final_key += ch

        for i in range(26):
            ch = chr(i + 65)
            if ch not in seen:
                final_key += ch

        self.prepared_key = final_key
        self.decrypt_mapping = {self.prepared_key[i]: chr(i + 65) for i in range(26)}
        return self.prepared_key

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        ciphertext = ""
        for c in plaintext:
            if c.isalpha():  # فقط الأحرف الأبجدية
                ciphertext += self.prepared_key[self.char_to_int(c)]
            else:
                ciphertext += c 
            #ciphertext += self.prepared_key[self.char_to_int(c)]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)
        plaintext = ""
        for c in ciphertext:
            plaintext += self.decrypt_mapping[c]
        return plaintext


