from BaseCipher import BaseCipher

class playfair(BaseCipher):
    def __init__(self, key):
        self.key = key

    def key_matrix(self, key):
        
