from .BaseCipher import BaseCipher

class DES(BaseCipher):
    def __init__(self, key: str):
        self.key = self._pad_key(key)

    def _pad_key(self, key):
        key = key.encode()
        return key.ljust(8, b'\0')[:8]

    def _pad_text(self, text):
        data = text.encode()
        pad_len = 8 - (len(data) % 8)
        return data + bytes([pad_len]) * pad_len

    def _unpad_text(self, data):
        pad_len = data[-1]
        return data[:-pad_len]

    def encrypt(self, plaintext: str):
        from Crypto.Cipher import DES as CryptoDES

        cipher = CryptoDES.new(self.key, CryptoDES.MODE_ECB)
        padded = self._pad_text(plaintext)
        encrypted = cipher.encrypt(padded)

        return encrypted.hex()

    def decrypt(self, ciphertext: str):
        from Crypto.Cipher import DES as CryptoDES

        cipher = CryptoDES.new(self.key, CryptoDES.MODE_ECB)
        decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
        return self._unpad_text(decrypted).decode()
