import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Crypto Algorithms")

method = st.selectbox("Method", ["caesar", "vigenere", 
                                 "hill", "playfair", 
                                 "premutation", "feistal",
                                   "mono", "otp", "rotor",
                                   "des", "aes"])
text = st.text_input("Text")
key = st.text_input("Key")

if st.button("Encrypt"):
    payload = {"method": method, "text": text, "key": key}
    response = requests.post(f"{API_URL}/encrypt", json=payload)
    res = response.json()  # JSON response
    if "result" in res:
        st.success("Ciphertext: " + res["result"])
    else:
        st.error("Error: " + res.get("error", "Unknown error"))

if st.button("Decrypt"):
    payload = {"method": method, "text": text, "key": key}
    response = requests.post(f"{API_URL}/decrypt", json=payload)
    res = response.json()
    if "result" in res:
        st.success("Plaintext: " + res["result"])
    else:
        st.error("Error: " + res.get("error", "Unknown error"))
