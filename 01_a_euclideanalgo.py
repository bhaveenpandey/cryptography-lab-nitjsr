# Bhaveen Pandey (2025PGCSIS18)
# Implementation of Euclidean Algorithm 

print("Euclidean Algorithm")

def gcd(a,b):
    if(a==0): return b
    else:
        return gcd(b%a,a)
        
        
a=int(input("Enter First Number : "))    
b=int(input("Enter Second Number : "))  

print("GCD = ",abs(gcd(a,b)))
