from .BaseCipher import BaseCipher


class Feistel(BaseCipher):
    def __init__(self, key):
        self.key = key
        self.key_bytes = None
        self.subkeys = None
        self.num_rounds = 8
        self.prepare_key()

    def prepare_key(self):
        """Convert key to bytes and generate subkeys"""
        key = self.normalize(self.key)
        self.key_bytes = [ord(c) for c in key]
        self.generate_subkeys()
        return self.key_bytes

    def generate_subkeys(self):
        """Generate round subkeys"""
        self.subkeys = []
        len_key = len(self.key_bytes)

        for i in range(self.num_rounds):
            rotated = self.key_bytes[(i % len_key):] + self.key_bytes[:(i % len_key)]
            subkey = [(x + i) % 256 for x in rotated]
            self.subkeys.append(subkey)

    @staticmethod
    def feistel_function(R, subkey):
        """Feistel round function"""
        result = []
        for i in range(len(R)):
            result.append(R[i] ^ subkey[i % len(subkey)])
        return result

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)

        if len(plaintext) % 2 != 0:
            plaintext += 'X'

        bits = [ord(c) for c in plaintext]
        left = bits[:len(bits) // 2]
        right = bits[len(bits) // 2:]

        for round_num in range(self.num_rounds):
            new_left = right
            f_result = self.feistel_function(right, self.subkeys[round_num])
            new_right = [left[i] ^ f_result[i] for i in range(len(left))]
            left, right = new_left, new_right

        final = left + right
        return "".join(chr(i % 256) for i in final)

    def decrypt(self, ciphertext):
        bits = [ord(c) for c in ciphertext]
        left = bits[:len(bits) // 2]
        right = bits[len(bits) // 2:]

        for round_num in range(self.num_rounds - 1, -1, -1):
            new_right = left
            f_result = self.feistel_function(left, self.subkeys[round_num])
            new_left = [right[i] ^ f_result[i] for i in range(len(right))]
            left, right = new_left, new_right

        final = left + right
        return "".join(chr(i % 256) for i in final)
