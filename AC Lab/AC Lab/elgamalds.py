import random
from math import gcd

def modinv(a, m):
    """Compute modular inverse of a mod m."""
    # Extended Euclidean Algorithm
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def is_prime(n):
    """Simple primality test for small numbers."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keys(p=None, alpha=None):
    """Key generation for ElGamal signature."""
    # For demonstration, use small primes; use large primes in real applications.
    if p is None:
        # Find a random prime p
        while True:
            p = random.randint(1000, 5000)
            if is_prime(p):
                break
    if alpha is None:
        # Find a primitive root alpha (generator)
        alpha = random.randint(2, p - 2)
    x = random.randint(1, p - 2)  # Private key
    y = pow(alpha, x, p)          # Public key component
    return (p, alpha, y, x)

def sign(p, alpha, x, m):
    """Generate ElGamal signature for message m."""
    while True:
        k = random.randint(1, p - 2)
        if gcd(k, p - 1) == 1:
            break
    r = pow(alpha, k, p)
    k_inv = modinv(k, p - 1)
    s = (k_inv * (m - x * r)) % (p - 1)
    return (r, s)

def verify(p, alpha, y, r, s, m):
    """Verify ElGamal signature (r, s) for message m."""
    if not (1 <= r <= p - 1):
        return False
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(alpha, m, p)
    return v1 == v2

# Example usage
if __name__ == "__main__":
    # Key generation
    p, alpha, y, x = generate_keys()
    print(f"Public key: (p={p}, alpha={alpha}, y={y})")
    print(f"Private key: x={x}")

    # Sign a message
    m = 1234  # Example message (should be < p-1)
    r, s = sign(p, alpha, x, m)
    print(f"Signature: r={r}, s={s}")

    # Verify signature
    valid = verify(p, alpha, y, r, s, m)
    print(f"Signature valid? {valid}")
