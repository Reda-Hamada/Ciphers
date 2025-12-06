from fastapi import FastAPI, HTTPException
from .schemas import CipherRequest
from crypto.caesar import Caser
from crypto.vigenere import VigenereCipher
from crypto.hill import HillCipher
from crypto.playfair import PlayfairCipher
from crypto.feistal import Feistel

app = FastAPI()


@app.post("/encrypt")
def encrypt(data: CipherRequest):
    method = data.method.lower()

    if method == "caesar":
        return {"result": Caser.encrypt(data.text, int(data.key))}

    if method == "vigenere":
        return {"result": VigenereCipher.encrypt(data.text, data.key)}

    if method == "hill":
        cipher = HillCipher(data.key)
        return {"result": cipher.encrypt(data.text)}

    if method == "playfair":
        cipher = PlayfairCipher(data.key)
        return {"result": cipher.encrypt(data.text)}

    if method == "feistal":
        cipher = Feistel(data.key)
        return {"result": cipher.encrypt(data.text)}

    raise HTTPException(400, "Invalid cipher method")
