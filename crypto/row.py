import random

def generate_random_key(length):
    """Generate a random key for row transposition (1..length, shuffled)."""
    key = list(range(1, length + 1))
    random.shuffle(key)
    return key

def encrypt(plain_text, key=None):
    """Encrypt plain_text using Row Transposition Cipher."""
    # Remove spaces and convert to uppercase
    plain_text = plain_text.replace(" ", "").upper()
    n = len(plain_text)

    # If key is not provided, generate a random key
    if key is None:
        # Default number of columns = min(5, length of text)
        cols = min(5, len(plain_text))
        key = generate_random_key(cols)
    else:
        cols = len(key)

    # Add padding 'X' to make the text fit into the grid
    while len(plain_text) % cols != 0:
        plain_text += "X"

    # Split text into a matrix (list of rows)
    matrix = [plain_text[i:i+cols] for i in range(0, len(plain_text), cols)]

    # Determine column order based on the key
    order = sorted(range(len(key)), key=lambda x: key[x]-1)

    # Read columns according to the key order
    cipher_text = ""
    for col_index in order:
        for row in matrix:
            cipher_text += row[col_index]

    return cipher_text, key

def decrypt(cipher_text, key):
    """Decrypt cipher_text using Row Transposition Cipher."""
    cipher_text = cipher_text.replace(" ", "").upper()
    cols = len(key)
    rows = len(cipher_text) // cols

    # Determine column order based on the key
    order = sorted(range(len(key)), key=lambda x: key[x]-1)

    # Create an empty matrix
    matrix = [[""] * cols for _ in range(rows)]

    # Fill the matrix column by column according to the key order
    index = 0
    for col_index in order:
        for row in range(rows):
            matrix[row][col_index] = cipher_text[index]
            index += 1

    # Read the rows to get the plaintext
    plain_text = "".join("".join(row) for row in matrix)
    return plain_text

# -------------------- TEST AREA --------------------
if __name__ == "__main__":
    # Ask user for input
    plain = input("Enter plain text: ").strip()
    key_input = input("Enter key as numbers separated by space (leave empty for random): ").strip()

    # Convert user input to list of integers if provided
    if key_input != "":
        key = [int(k) for k in key_input.split()]
    else:
        key = None

    # Encrypt the plaintext
    cipher, used_key = encrypt(plain, key)
    print("Cipher Text:", cipher)
    print("Used Key:", used_key)

    # Decrypt back to plaintext
    print("Decrypted:", decrypt(cipher, used_key))
