from streamlit import secrets
from .BaseCipher import BaseCipher

import random
import string


class OneTimePad(BaseCipher):
    def __init__(self, key=None):
        self.key = key
        self.prepared_key = None

    def prepare_key(self):
        """Key validation - will be generated per message if not provided"""
        if self.key:
            self.prepared_key = self.normalize(self.key)
        return self.prepared_key

    @staticmethod
    def generate_random_key(length):
        """Generate random key of given length"""
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

    def encrypt(self, plaintext):
        plaintext_bytes = plaintext.encode('utf-8')
        if not self.key or len(self.key) != len(plaintext_bytes):
            key_bytes = secrets.token_bytes(len(plaintext_bytes))
        else:
            key_bytes = self.key.encode('utf-8')
            ciphertext_bytes = bytes([p ^ k for p, k in zip(plaintext_bytes, key_bytes)])
        self.prepared_key = key_bytes
        return ciphertext_bytes.hex()  # أو base64 للتمثيل النصي

        plaintext = self.normalize(plaintext)

        # Generate key if not provided
        if not self.key or len(self.key) != len(plaintext):
            key = self.generate_random_key(len(plaintext))
        else:
            key = self.normalize(self.key)

        ciphertext = ""
        for p, k in zip(plaintext, key):
            c = self.int_to_char(self.char_to_int(p) + self.char_to_int(k))
            ciphertext += c

        # Store the key for potential reuse
        self.prepared_key = key
        return ciphertext

    def decrypt(self, ciphertext):
        if not self.prepared_key:
            raise ValueError("No key available for decryption")

        ciphertext = self.normalize(ciphertext)
        key = self.prepared_key

        plaintext = ""
        for c, k in zip(ciphertext, key):
            p = self.int_to_char(self.char_to_int(c) - self.char_to_int(k))
            plaintext += p

        return plaintext

    def get_key(self):
        """Return the key used for encryption"""
        return self.prepared_key
