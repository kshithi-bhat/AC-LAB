def is_prime(n):
    """Simple primality test for small numbers"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def mod_inverse(a, m):
    """Find modular inverse using extended Euclidean algorithm"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # inverse doesn't exist
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = extended_gcd(b % a, a)
    return (g, x - (b // a) * y, y)

def rsa_key_generation(p, q):
    """Generate RSA keys from primes p and q"""
    assert is_prime(p) and is_prime(q), "Both numbers must be prime"
    
    n = p * q
    phi = (p-1) * (q-1)
    
    # Choose e (public exponent)
    e = 7  # common choice for small primes
    while extended_gcd(e, phi)[0] != 1:
        e += 1
    
    # Compute private exponent d
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def rsa_encrypt(m, public_key):
    """Encrypt message using public key"""
    e, n = public_key
    return pow(m, e, n)

def rsa_decrypt(c, private_key):
    """Decrypt ciphertext using private key"""
    d, n = private_key
    return pow(c, d, n)

# Example usage with small primes
p, q = 11, 13  # Must be prime
public_key, private_key = rsa_key_generation(p, q)

# Original messages
m1 = 9
m2 = 11

# Encrypt messages
c1 = rsa_encrypt(m1, public_key)
c2 = rsa_encrypt(m2, public_key)

# Homomorphic multiplication
c_product = (c1 * c2) % public_key[1]

# Decrypt product
decrypted_product = rsa_decrypt(c_product, private_key)

print(f"Original product: {m1 * m2}")
print(f"Decrypted product: {decrypted_product}")
