from BaseCipher import BaseCipher


class oneTime(BaseCipher):
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass
import random
import string

def generate_random_key(length):
    """Generate a random key of uppercase letters."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(plain_text, key=None):
    """Encrypt plain_text using OTP. If key not provided, create random one."""
    plain_text = plain_text.upper()

    # Generate random key if user didn't provide one
    if not key:
        key = generate_random_key(len(plain_text))
    else:
        key = key.upper()
        if len(key) != len(plain_text):
            raise ValueError("Key length must match plain text length!")

    cipher = ""
    for p, k in zip(plain_text, key):
        c = (ord(p) - 65 + (ord(k) - 65)) % 26
        cipher += chr(c + 65)

    return cipher, key

def decrypt(cipher_text, key):
    """Decrypt cipher_text using OTP and provided key."""
    cipher_text = cipher_text.upper()
    key = key.upper()

    plain = ""
    for c, k in zip(cipher_text, key):
        p = (ord(c) - 65 - (ord(k) - 65)) % 26
        plain += chr(p + 65)

    return plain

# -------------------- TEST AREA  --------------------
if __name__ == "__main__":
    plain = input("Enter plain text: ").strip().upper()
    key = input("Enter key (leave empty for random): ").strip()

    cipher, used_key = encrypt(plain, key if key != "" else None)

    print("Cipher Text:", cipher)
    print("Used Key:", used_key)
    print("Decrypted:", decrypt(cipher, used_key))
