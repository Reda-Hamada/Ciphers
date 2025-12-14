from Crypto.Cipher import AES as PyAES
from Crypto.Util.Padding import pad, unpad
import base64
from .BaseCipher import BaseCipher

class AES(BaseCipher):
    def __init__(self, key: str):
        """
        key: string من المستخدم
        AES-128/192/256 => 16, 24, 32 bytes
        """
        self.key_str = key
        self.key = key.encode("utf-8")  # تحويل string ل bytes
        if len(self.key) not in (16, 24, 32):
            raise ValueError("AES key must be 16, 24, or 32 bytes")
        self.iv = None  # لتخزين IV لو احتاج لاحقًا

    def prepare_key(self):
        # لو حبيت تعمل حاجة قبل التشفير، حاليا مش محتاج
        pass

    def encrypt(self, plaintext: str) -> str:
        try:
            cipher = PyAES.new(self.key, PyAES.MODE_CBC)
            self.iv = cipher.iv
            ct_bytes = cipher.encrypt(pad(plaintext.encode(), PyAES.block_size))
            ciphertext = self.iv + ct_bytes
            return base64.b64encode(ciphertext).decode()
        except Exception as e:
            raise ValueError(f"AES Encryption failed: {str(e)}")

    def decrypt(self, ciphertext: str) -> str:
        try:
            raw = base64.b64decode(ciphertext)
            iv = raw[:16]
            ct = raw[16:]
            cipher = PyAES.new(self.key, PyAES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ct), PyAES.block_size)
            return plaintext.decode()
        except Exception as e:
            raise ValueError(f"AES Decryption failed: {str(e)}")
