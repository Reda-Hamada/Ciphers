from fastapi import FastAPI, HTTPException
from .schemas import CipherRequest
from crypto.caesar import Caesar
from crypto.vigenere import Vigenere
from crypto.hill import HillCipher
from crypto.playfair import PlayfairCipher
from crypto.feistal import Feistel

app = FastAPI()

@app.post("/encrypt")
def encrypt(data: CipherRequest):
    method = data.method.lower()

    if method == "caesar":
        cas = Caesar((int(data.key)))
        return {"result": cas.encrypt(data.text)}

    if method == "vigenere":
        vig = Vigenere(data.key)
        return {"result": vig.encrypt(data.text)}

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
