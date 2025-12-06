from .BaseCipher import BaseCipher


class Rotor(BaseCipher):
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


class RotorMachine:
    def __init__(self):
        self.rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        self.rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
        self.rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")

    def rotate_rotors(self):
        self.rotor1.rotate()

        if self.rotor1.offset == 0:
            self.rotor2.rotate()

        if self.rotor2.offset == 0:
            self.rotor3.rotate()

    def encrypt_char(self, c):
        if not c.isalpha():
            return c

        c = c.upper()

        c = self.rotor1.forward(c)
        c = self.rotor2.forward(c)
        c = self.rotor3.forward(c)

        self.rotate_rotors()

        return c

    def decrypt_char(self, c):
        if not c.isalpha():
            return c

        c = c.upper()

        c = self.rotor3.backward(c)
        c = self.rotor2.backward(c)
        c = self.rotor1.backward(c)

        self.rotate_rotors()

        return c

    def encrypt(self, text):
        result = ""
        for ch in text:
            result += self.encrypt_char(ch)
        return result

    def decrypt(self, text):

        self.rotor1.offset = 0
        self.rotor2.offset = 0
        self.rotor3.offset = 0

        result = ""
        for ch in text:
            result += self.decrypt_char(ch)
        return result


if __name__ == "__main__":
    machine = RotorMachine()

    text = input("Enter plaintext: ")
    cipher = machine.encrypt(text)
    print("Ciphertext:", cipher)

    machine = RotorMachine()
    plain = machine.decrypt(cipher)
    print("Decrypted:", plain)
