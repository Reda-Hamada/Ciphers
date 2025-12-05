from BaseCipher import BaseCipher

class HillCipher(BaseCipher):
    def __init__(self, key):
        """
        key is a string have the 4 chars.
        :param key:
        """
        self.key = key
