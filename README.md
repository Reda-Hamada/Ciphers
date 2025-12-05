# 🔐 Cypher — Cryptography Algorithms Toolkit  
A clean and modular implementation for classic encryption algorithms using **Python**, **FastAPI**, and a simple GUI.

---

## 📌 Overview
This project provides a unified structure for multiple classical ciphers including:

- **Caesar Cipher**
- **Vigenère Cipher**
- **Hill Cipher**
- **Monoalphabetic Cipher**
- **Transposition Cipher**

The goal is to create a reusable, modular, and testable cryptography toolkit with a REST API built using **FastAPI**, and a GUI for demonstration.

---

## 🧱 Project Structure

Cypher/
│
├── backend/
│   ├── main.py        # FastAPI entry point
│   ├── routers/
│   │   ├── caesar.py
│   │   ├── vigenere.py
│   │   └── hill.py
│   │
│   ├── schemas/
│   │   └── crypto.py
│   │
│   └── core/
│       └── config.py
│
├── crypto/
│   ├── caesar.py
│   ├── vigenere.py
│   └── hill.py
│
├── gui/
│   └── app.py         # Streamlit GUI
│
├── tests/
│   └── test_caesar.py
│
├── README.md
├── requirements.txt
└── .gitignore

