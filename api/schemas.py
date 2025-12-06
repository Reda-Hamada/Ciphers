from pydantic import BaseModel, Field

class CipherRequest(BaseModel):
    method: str = Field(..., description="Cipher method (caesar, vigenere, hill, playfair, mono, ..., DES)")
    text: str = Field(..., description="Plaintext or ciphertext")
    key: str = Field(..., description="Key used in encryption/decryption")


class CipherResponse(BaseModel):
    result: str = Field(..., description="Encrypted or decrypted output")
    method: str = Field(..., description="Cipher used")
