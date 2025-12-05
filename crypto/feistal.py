from BaseCipher import BaseCipher


class Feistel(BaseCipher):
    def __init__(self, key):
        key = self.normalize(key)
        self.key = [ord(c) for c in key]
        self.num_of_round = 8
        self.generate_subkey()

    def generate_subkey(self):
        self.subkey = []
        len_key = len(self.key)

        for i in range(self.num_of_round):
            rotated = self.key[(i % len_key):] + self.key[:(i % len_key)]
            subkey = [(x + i) % 256 for x in rotated]
            self.subkey.append(subkey)

    @staticmethod
    def feistalFunc(R, subkey):
        result = []
        for i in range(len(R)):
            result.append(R[i] ^ subkey[i % len(subkey)])
        return result

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)
        length = len(plaintext)

        if length % 2 != 0:
            plaintext += '0'
            length += 1

        bits = [ord(c) for c in plaintext]
        left = bits[:length // 2]
        right = bits[length // 2:]

        for round_num in range(self.num_of_round):
            new_left = right
            f_result = self.feistalFunc(right, self.subkey[round_num])

            new_right = []
            for i in range(len(left)):
                new_right.append(left[i] ^ f_result[i])

            left = new_left
            right = new_right

        final = left + right
        ciphertext = "".join(chr(i % 256) for i in final)
        return ciphertext

    def decrypt(self, ciphertext):
        length = len(ciphertext)

        bits = [ord(c) for c in ciphertext]
        left = bits[:length // 2]
        right = bits[length // 2:]

        for round_num in range(self.num_of_round - 1, -1, -1):
            new_right = left

            f_result = self.feistalFunc(left, self.subkey[round_num])

            new_left = []
            for i in range(len(right)):
                new_left.append(right[i] ^ f_result[i])

            left = new_left
            right = new_right

        final = left + right
        plaintext = "".join(chr(i % 256) for i in final)
        return plaintext