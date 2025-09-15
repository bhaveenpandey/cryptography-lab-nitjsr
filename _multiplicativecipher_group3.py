#multiplicativecipher 
#Code Word - UWEEWGNMGUZBYXY

#Decrypted Text - missioncomplete
#Key - 19 


def decrypt_multiplicative(ciphertext):
    # Convert ciphertext to lowercase
    ciphertext = ciphertext.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    # Possible keys: numbers coprime with 26
    possible_keys = [k for k in range(1, 26) if gcd(k, 26) == 1]

    for key in possible_keys:
        decrypted_text = ""
        key_inv = mod_inverse(key, 26)

        for char in ciphertext:
            if char.isalpha():
                c = alphabets.index(char)
                p = (c * key_inv) % 26
                decrypted_text += alphabets[p]
            else:
                decrypted_text += char

        print(f"Key = {key} → {decrypted_text}")


def gcd(a, b):
    """Find GCD using Euclid's algorithm"""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """Find modular multiplicative inverse using brute force"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# Example usage
cipher = input("Enter the ciphertext: ")
decrypt_multiplicative(cipher)
