def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return (x, y)

def encryption(P, n):
    return (P ** 2) % n

def decryption(cipher, p, q, n):
    zp, zq = extended_gcd(p, q)
    
    # Compute square roots modulo p and q
    a1 = pow(cipher, (p + 1) // 4, p)
    a2 = p - a1  # Additional root
    b1 = pow(cipher, (q + 1) // 4, q)
    b2 = q - b1  # Additional root
    
    # Combine using CRT
    p1 = (zp * p * b1 + zq * q * a1) % n
    p2 = (zp * p * b1 + zq * q * a2) % n
    p3 = (zp * p * b2 + zq * q * a1) % n
    p4 = (zp * p * b2 + zq * q * a2) % n
    
    return p1, p2, p3, p4

p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
n = p * q
print(n)
P = int(input("Enter plaintext: "))

cipher = encryption(P, n)
print(f"Ciphertext is: {cipher}")

plaintexts = decryption(cipher, p, q, n)
print(f"Possible decrypted plaintexts are: {plaintexts}")
