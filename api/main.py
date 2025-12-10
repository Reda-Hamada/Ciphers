from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from crypto.mono import MonoCipher
from crypto.one_time import OneTimePad
from crypto.premutation import RowTranspositionCipher
from .schemas import CipherRequest
from crypto.caesar import Caesar
from crypto.vigenere import Vigenere
from crypto.hill import HillCipher
from crypto.playfair import PlayfairCipher
from crypto.feistal import Feistel
from crypto.rotor import RotorMachine

app = FastAPI()

@app.post("/encrypt")
def encrypt(data: CipherRequest):
    method = data.method.lower()
    try:
        if method == "caesar":
            cas = Caesar(int(data.key))
            result = cas.encrypt(data.text)

        elif method == "vigenere":
            vig = Vigenere(data.key)
            result = vig.encrypt(data.text)

        elif method == "hill":
            cipher = HillCipher(data.key)
            result = cipher.encrypt(data.text)

        elif method == "playfair":
            cipher = PlayfairCipher(data.key)
            result = cipher.encrypt(data.text)

        elif method == "feistal":
            cipher = Feistel(data.key)
            result = cipher.encrypt(data.text)

        elif method == "premutation":
            cipher = RowTranspositionCipher(data.key)
            result = cipher.encrypt(data.text)

        elif method == "mono":
            cipher = MonoCipher(data.key)
            result = cipher.encrypt(data.text)

        elif method == "otp":
            cipher = OneTimePad(data.key)
            result = cipher.encrypt(data.text)
        
        elif method == "rotor":
            cipher = RotorMachine(data.key)
            result = cipher.encrypt(data.text)
        else:
            raise HTTPException(status_code=400, detail="Invalid cipher method")

        return {"result": result}

    except Exception as e:
        return {"error": str(e)}
    
@app.post("/decrypt")
def decrypt(data: CipherRequest):
    method = data.method.lower()
    try:
        if method == "caesar":
            cas = Caesar(int(data.key))
            result = cas.decrypt(data.text)

        elif method == "vigenere":
            vig = Vigenere(data.key)
            result = vig.decrypt(data.text)

        elif method == "hill":
            cipher = HillCipher(data.key)
            result = cipher.decrypt(data.text)

        elif method == "playfair":
            cipher = PlayfairCipher(data.key)
            result = cipher.decrypt(data.text)

        elif method == "feistal":
            cipher = Feistel(data.key)
            result = cipher.decrypt(data.text)

        elif method == "premutation":
            cipher = RowTranspositionCipher(data.key)
            result = cipher.decrypt(data.text)

        elif method == "mono":
            cipher = MonoCipher(data.key)
            result = cipher.decrypt(data.text)

        elif method == "otp":
            cipher = OneTimePad(data.key)
            # تأكد من وجود prepared_key قبل فك التشفير
            cipher.prepare_key()
            result = cipher.decrypt(data.text)

        else:
            raise HTTPException(status_code=400, detail="Invalid cipher method")

        return {"result": result}

    except Exception as e:
        return {"error": str(e)}

# def encrypt(data: CipherRequest):
    # method = data.method.lower()
    # try:

    # if method == "caesar":
    #     cas = Caesar((int(data.key)))
    #     return {"result": cas.encrypt(data.text)}

    # if method == "vigenere":
    #     vig = Vigenere(data.key)
    #     return {"result": vig.encrypt(data.text)}

    # if method == "hill":
    #     cipher = HillCipher(data.key)
    #     return {"result": cipher.encrypt(data.text)}

    # if method == "playfair":
    #     cipher = PlayfairCipher(data.key)
    #     return {"result": cipher.encrypt(data.text)}

    # if method == "feistal":
    #     cipher = Feistel(data.key)
    #     return {"result": cipher.encrypt(data.text)}
    
    # if method == "premutation":
    #     cipher = RowTranspositionCipher(data.key)
    #     return {"result": cipher.encrypt(data.text)}
    
    # if method == "Mono":
    #     cipher = MonoCipher(data.key)
    #     return {"result": cipher.encrypt(data.text)}
    
    # if method == "One Time Pad":
    #     cipher = OneTimePad(data.key)
    #     return {"result": cipher.encrypt(data.text)}

    # raise HTTPException(400, "Invalid cipher method")
