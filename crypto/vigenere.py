from BaseCipher import BaseCipher


class VigenereCipher(BaseCipher):
    def __init__(self, key):
        self.key = self.normalize(key)

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            if char.isalpha():
                p = self.char_to_int(char)
                shift= self.char_to_int(self.key[key_index % len(self.key)])
                c = self.int_to_char(p + shift)
                ciphertext += c
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)
        plaintext = ""
        key_index = 0

        for char in ciphertext:
            if char.isalpha():
                c = self.char_to_int(char)
                shift = self.char_to_int(self.key[key_index % len(self.key)])
                p = self.int_to_char(c - shift)
                plaintext += p
                key_index += 1
            else:
                plaintext += char
        return plaintext


    