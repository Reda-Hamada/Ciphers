import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Crypto Algorithms")

method = st.selectbox("Method", ["caesar", "vigenere", 
                                 "hill", "playfair", 
                                 "premutation", "feistal",
                                   "mono", "otp", "rotor"])
text = st.text_input("Text")
key = st.text_input("Key")

if st.button("Encrypt"):
    payload = {
        "method": method,
        "text": text,
        "key": key
    }
    response = requests.post(f"{API_URL}/encrypt", json=payload)
    st.write("Ciphertext:", response.json()["result"])

if st.button("Decrypt"):
    payload = {
        "method": method,
        "text": text,
        "key": key
    }
    response = requests.post(f"{API_URL}/decrypt", json=payload)
    st.write("Plaintext:", response.json()["result"])
