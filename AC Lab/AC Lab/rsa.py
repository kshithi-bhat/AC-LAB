def encryption(M, e, n):
    return (M**e)%n

def decryption(cipher, d, n):
    return (cipher**d)%n

def inverse(a, n):
    b=2
    while((a*b)%n)!=1:
        b+=1
    return b

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
M = int(input("Enter the value of M: "))
n = p*q
phi = (p-1)*(q-1)
e = int(input("Enter value of e: "))

#d.e mod phi = 1
d = inverse(e, phi)

cipher = encryption(M, e, n)
print(f"Ciphertext is: {cipher}")

plain = decryption(cipher, d, n)
print(f"Plaintext is: {plain}")



# import math

# def extended_gcd(a, b):
#     """Returns (gcd, x, y) such that a*x + b*y = gcd"""
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = extended_gcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     """Returns modular inverse of a mod m, or raises ValueError if none exists"""
#     g, x, y = extended_gcd(a, m)
#     if g != 1:
#         raise ValueError(f"No modular inverse for {a} mod {m}")
#     return x % m

# def is_prime(n):
#     """Checks primality by trial division up to sqrt(n)"""
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     for i in range(5, int(math.isqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def generate_keys():
#     # Small primes for demonstration; use large primes in real applications!
#     p, q = 61, 53
#     if not (is_prime(p) and is_prime(q)):
#         raise ValueError("p and q must be prime.")
#     n = p * q
#     phi = (p - 1) * (q - 1)
#     e = 17
#     while math.gcd(e, phi) != 1:
#         e += 2
#     d = modinv(e, phi)
#     return (e, n), (d, n)

# def encrypt(message, public_key):
#     e, n = public_key
#     return pow(message, e, n)

# def decrypt(ciphertext, private_key):
#     d, n = private_key
#     return pow(ciphertext, d, n)

# # Example usage
# public_key, private_key = generate_keys()
# message = 42

# ciphertext = encrypt(message, public_key)
# decrypted = decrypt(ciphertext, private_key)

# print("Public key:", public_key)
# print("Private key:", private_key)
# print("Original message:", message)
# print("Encrypted (ciphertext):", ciphertext)
# print("Decrypted:", decrypted)



