from .BaseCipher import BaseCipher


class Rotor:
    def __init__(self, wiring):
        self.wiring = wiring
        self.offset = 0

    def rotate(self):
        self.offset = (self.offset + 1) % 26

    def forward(self, c):
        index = (ord(c) - ord('A') + self.offset) % 26
        return self.wiring[index]

    def backward(self, c):
        index = self.wiring.index(c)
        return chr((index - self.offset) % 26 + ord('A'))


class RotorMachine(BaseCipher):
    def __init__(self, key=None):
        self.key = key
        self.rotor1 = None
        self.rotor2 = None
        self.rotor3 = None
        self.prepare_key()

    def prepare_key(self):
        """Initialize rotors with standard wirings"""
        self.rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        self.rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
        self.rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
        
        if self.key and len(self.key) >= 3:
            self.rotor1.offset = ord(self.key[0].upper()) - ord('A')
            self.rotor2.offset = ord(self.key[1].upper()) - ord('A')
            self.rotor3.offset = ord(self.key[2].upper()) - ord('A')
        
        return [self.rotor1, self.rotor2, self.rotor3]

    def rotate_rotors(self):
        """Rotate rotors (with turnover)"""
        self.rotor1.rotate()
        if self.rotor1.offset == 0:
            self.rotor2.rotate()
        if self.rotor2.offset == 0:
            self.rotor3.rotate()

    def encrypt(self, plaintext):
        plaintext = self.normalize(plaintext)

        # Reset rotors
        self.rotor1.offset = 0
        self.rotor2.offset = 0
        self.rotor3.offset = 0

        ciphertext = ""
        for c in plaintext:
            c = self.rotor1.forward(c)
            c = self.rotor2.forward(c)
            c = self.rotor3.forward(c)
            ciphertext += c
            self.rotate_rotors()

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self.normalize(ciphertext)

        # Reset rotors
        self.rotor1.offset = 0
        self.rotor2.offset = 0
        self.rotor3.offset = 0

        plaintext = ""
        for c in ciphertext:
            c = self.rotor3.backward(c)
            c = self.rotor2.backward(c)
            c = self.rotor1.backward(c)
            plaintext += c
            self.rotate_rotors()

        return plaintext

