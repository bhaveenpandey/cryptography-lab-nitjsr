#ciphertext to plain text
#AdditiveCipher
#CaesarCipher
#BruteForce


def additive_brute_force(cipher_text):
    cipher_text = cipher_text.upper()  
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 # Try all possible keys from 0 to 25
    print("Brute Force Results:\n")
    for key in range(26):  # Try all possible keys from 0 to 25
        decrypted_text = ""

        for char in cipher_text:
            if char.isalpha():
                # Decrypt character: (position - key) mod 26
                decrypted_text += alphabet[(alphabet.index(char) - key) % 26]
            else:
                decrypted_text += char 

        print(f"Key = {key}: {decrypted_text}")

cipher = input("Enter the cipher text: ")
additive_brute_force(cipher)



#CIPHERTEXT - MKTGLFBMHKWXKLGHP
#KEY- 19
#PLAINTEXT - TRANSMITORDERNOW
