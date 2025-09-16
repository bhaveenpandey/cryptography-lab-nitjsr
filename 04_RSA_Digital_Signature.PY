# RSA Digital Signature without external libraries

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def powmod(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

# ---- Key Generation (toy primes for demo) ----
p, q = 61, 53
n = p * q
phi = (p-1)*(q-1)
e = 17
d = modinv(e, phi)

print("Public Key (e,n):", (e, n))
print("Private Key (d,n):", (d, n))

# ---- User Input ----
msg = int(input("Enter a number message to sign: "))

# ---- Signing ----
signature = powmod(msg, d, n)
print("Digital Signature:", signature)

# ---- Verification ----
check = powmod(signature, e, n)
if check == msg:
    print("✅ Signature Verified")
else:
    print("❌ Verification Failed")

