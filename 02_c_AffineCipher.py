#AffineCipher
#Bhaveen Pandey (2025PGCSIS18)



# Function to find multiplicative inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None 

# Encryption function
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            x = ord(char) - ord(base)
            enc = (a * x + b) % 26
            result += chr(enc + ord(base))
        else:
            result += char
    return result

# Decryption function
def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Invalid 'a'! It must be coprime with 26.")
    
    for char in cipher:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            y = ord(char) - ord(base)
            dec = (a_inv * (y - b)) % 26
            result += chr(dec + ord(base))
        else:
            result += char
    return result

#Taking input from user 
plaintext = input("Enter the Message : ")
a=int(input("Enter key 'a' : "))
b=int(input("Enter key 'b' : "))

# Encrypting
cipher = affine_encrypt(plaintext, a, b)
print(f"\nEncrypted Text: {cipher}")

# Decrypting
decrypted = affine_decrypt(cipher, a, b)
print(f"Decrypted Text: {decrypted}")
