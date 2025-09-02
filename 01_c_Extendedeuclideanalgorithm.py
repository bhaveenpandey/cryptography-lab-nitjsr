#Bhaveen Pandey (2025PGCSIS18)
#Extended Euclidean Algorithm

#function defining
def extended_euclidean(a, b):
    # Base Case
    if b == 0:
        return a, 1, 0  # gcd, x, y

    # Recursive Call
    gcd, x1, y1 = extended_euclidean(b, a % b)

    # Update x and y using results of recursive call
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y



a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

gcd, x, y = extended_euclidean(a, b)

print(f"GCD of {a} and {b} = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")
