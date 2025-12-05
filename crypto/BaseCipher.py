class BaseCipher:
    def encrypt(self, plaintext):
        raise NotImplementedError

    def decrypt(self, ciphertext):
        raise NotImplementedError

    def prepare_key(self):
        raise NotImplementedError

    def normalize(self, text):
        return text.replace(" ","").upper()

    def char_to_int(self, c):
        return ord(c) - 65

    def int_to_char(self, i):
        return chr((i%26) + 65)