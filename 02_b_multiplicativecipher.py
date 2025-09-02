#Multiplicative_Cipher 
#Bhaveen Pandey (2025PGCSIS18)



# multiplicative_cipher.py

# Encryption:  C = (a * P) mod 26
# Decryption: P = (a_inv * C) mod 26, where a_inv is modular inverse of a (mod 26)

# Multiplicative Cipher
# Encryption:  C = (a * P) mod 26
# Decryption:  P = (a_inv * C) mod 26

ALPHABET_SIZE = 26

# Function to find GCD using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Inverse doesn't exist

# Encrypt function
def encrypt(plaintext, key):
    if gcd(key, ALPHABET_SIZE) != 1:
        raise ValueError("Invalid key! Key must be coprime with 26.")
    
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            # Formula: C = (P * key) mod 26
            ciphertext += chr(((ord(ch) - ord(base)) * key) % ALPHABET_SIZE + ord(base))
        else:
            ciphertext += ch
    return ciphertext

# Decrypt function
def decrypt(ciphertext, key):
    if gcd(key, ALPHABET_SIZE) != 1:
        raise ValueError("Invalid key! Key must be coprime with 26.")
    
    plaintext = ""
    inv_key = mod_inverse(key, ALPHABET_SIZE)
    if inv_key is None:
        raise ValueError("No modular inverse exists for the given key.")
    
    for ch in ciphertext:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            # Formula: P = (C * key^-1) mod 26
            plaintext += chr(((ord(ch) - ord(base)) * inv_key) % ALPHABET_SIZE + ord(base))
        else:
            plaintext += ch
    return plaintext

# Example usage
if __name__ == "__main__":
    key = 5  # Must be coprime with 26
    text = "Hello World"

    cipher = encrypt(text, key)
    decrypted = decrypt(cipher, key)

    print("Key:", key)
    print("Plaintext:", text)
    print("Ciphertext:", cipher)
    print("Decrypted:", decrypted)
