#2025PGCSIS18
#RSA

# Function to find gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# RSA Key Generation (fixed primes)
def generate_keys():
    p, q = 61, 53  
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17          
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Encryption
def encrypt(msg, pub_key):
    e, n = pub_key
    return [pow(ord(ch), e, n) for ch in msg]

# Decryption
def decrypt(cipher, priv_key):
    d, n = priv_key
    return ''.join([chr(pow(c, d, n)) for c in cipher])


public_key, private_key = generate_keys()
message = input("Enter a message: ")

cipher = encrypt(message, public_key)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, private_key))
