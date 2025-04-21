# Install required library
# pip install ecdsa

from ecdsa import SigningKey, NIST256p
import hashlib

# 1. Generate ECDSA key pair
private_key = SigningKey.generate(curve=NIST256p)  # secp256r1 curve
public_key = private_key.verifying_key

# 2. Message to sign (bytes)
message = b"Critical blockchain transaction 2025-04-22"

# 3. Sign message (automatically hashes with SHA-256)
signature = private_key.sign(message, hashfunc=hashlib.sha256)

print("Signature (hex):", signature.hex())

# 4. Verify signature
try:
    public_key.verify(signature, message, hashfunc=hashlib.sha256)
    print("Signature is valid")
except:
    print("Signature is invalid")











import random

def modinv(a, m):
    """Modular inverse using Extended Euclidean Algorithm"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = extended_gcd(b % a, a)
    return (g, x - (b // a) * y, y)

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, point):
        if point is None:
            return True
        x, y = point
        return (y*y - (x*x*x + self.a*x + self.b)) % self.p == 0

    def point_add(self, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            if y1 != y2:
                return None
            m = (3 * x1*x1 + self.a) * modinv(2*y1, self.p)
        else:
            m = (y2 - y1) * modinv(x2 - x1, self.p)

        m %= self.p
        x3 = (m*m - x1 - x2) % self.p
        y3 = (m*(x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_mult(self, k, point):
        result = None
        current = point
        while k > 0:
            if k % 2:
                result = self.point_add(result, current)
            current = self.point_add(current, current)
            k //= 2
        return result

class ECDSA:
    def __init__(self, curve, G, n):
        self.curve = curve
        self.G = G
        self.n = n

    def generate_keypair(self):
        private_key = random.randint(1, self.n-1)
        public_key = self.curve.scalar_mult(private_key, self.G)
        return private_key, public_key

    def sign(self, private_key, message_hash):
        while True:
            k = random.randint(1, self.n-1)
            R = self.curve.scalar_mult(k, self.G)
            if R is None:
                continue
            r = R[0] % self.n
            if r == 0:
                continue
            s = (modinv(k, self.n) * (message_hash + private_key*r)) % self.n
            if s != 0:
                return (r, s)

    def verify(self, public_key, message_hash, signature):
        r, s = signature
        if not (1 <= r < self.n and 1 <= s < self.n):
            return False
        
        w = modinv(s, self.n)
        u1 = (message_hash * w) % self.n
        u2 = (r * w) % self.n
        
        P = self.curve.point_add(
            self.curve.scalar_mult(u1, self.G),
            self.curve.scalar_mult(u2, public_key)
        )
        return P is not None and P[0] % self.n == r

# Verified parameters for secp192r1 (NIST P-192)
p = 6277101735386680763835789423207666416083908700390324961279
a = -3
b = 0x64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1
G = (0x188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012,
     0x07192B95FFC8DA78631011ED6B24CDD573F977A11E794811)
n = 6277101735386680763835789423176059013767194773182842284081

curve = EllipticCurve(a, b, p)
ecdsa = ECDSA(curve, G, n)

# Key generation
private_key, public_key = ecdsa.generate_keypair()
print(f"Private key: {private_key}")
print(f"Public key valid? {curve.is_on_curve(public_key)}")

# Signing
message_hash = 0x2efd9e4d131e1d6d9a9c38a4f2d231f3  # Example hash
signature = ecdsa.sign(private_key, message_hash)
print(f"Signature: ({hex(signature[0])}, {hex(signature[1])})")

# Verification
valid = ecdsa.verify(public_key, message_hash, signature)
print(f"Signature valid? {valid}")

