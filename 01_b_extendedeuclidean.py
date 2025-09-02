#Bhaveen Pandey(2025PGCSIS18)

# Extended Euclidean Algorithm in Python


def extended_euclidean(a, b):
    print(f"\nLet's find GCD of {a} and {b} using Extended Euclidean Algorithm...\n")
    
    # Initial values for coefficients
    old_r, r = a, b  
    old_s, s = 1, 0  
    old_t, t = 0, 1  

    step = 1
    
    while r != 0:
        quotient = old_r // r

        print(f"Step {step}:")
        print(f"Quotient = {old_r} // {r} = {quotient}")
        print(f"Updating values...")

        # Update remainders and coefficients
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

        print(f"Remainders: old_r = {old_r}, r = {r}")
        print(f"Coefficients: s = {old_s}, t = {old_t}")
        print("-" * 50)
        step += 1

    # Final result
    print(f"\nGCD = {old_r}")
    print(f"Coefficients: x = {old_s}, y = {old_t}")
    print(f"Verification: {a}*({old_s}) + {b}*({old_t}) = {a*old_s + b*old_t}")

    return old_r, old_s, old_t

# Taking input from the user
a = int(input("Enter the first number : \n"))
b = int(input("Enter the second number : \n"))

gcd, x, y = extended_euclidean(a, b)

print(f"\nFinal Answer:\nGCD({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
