#Additive(Ceasar) Cipher 
#Bhaveen Pandey (2025PGCSIS18)

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - shift + key) % 26 + shift)
        else:
            ciphertext += char  # Keep spaces and special chars unchanged
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - shift - key) % 26 + shift)
        else:
            plaintext += char
    return plaintext


# ---- Driver Code ----
message = input("Enter your message: ")
key = int(input("Enter key (0-25): "))

encrypted = encrypt(message, key)
print(f"Encrypted Message: {encrypted}")

decrypted = decrypt(encrypted, key)
print(f"Decrypted Message: {decrypted}")
