from BaseCipher import BaseCipher

class MonoCipher(BaseCipher):
    def __init__(self, key):
        key.upper()

        seen = set()
        final_key = ""
        for ch in key:
            if ch not in seen:
                seen.add(ch)
                final_key += ch

        for i in range(26):
            ch = chr(i+65)
            if ch not in seen:
                final_key += ch

        self.key = final_key
        self.decrypt_mapping = {self.key[i] : chr(i + 65) for i in range(26)}

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)

        ciphertext = ""
        for c in plaintext:
            ciphertext += self.key[self.char_to_int(c) - 65]

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)

        plaintext = ""
        for c in ciphertext:
            plaintext += self.decrypt_mapping[c]

        return plaintext
