def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def generate_keys():
    # For demo: use small primes; for real use, use large primes!
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    while gcd(e, phi) != 1:
        e += 2
    d = modinv(e, phi)
    return (e, n), (d, n)

def sign(message, private_key):
    d, n = private_key
    # For real applications, sign a hash of the message!
    return pow(message, d, n)

def verify(message, signature, public_key):
    e, n = public_key
    return message == pow(signature, e, n)

# Demo
public_key, private_key = generate_keys()
message = 65  # Should be less than n

signature = sign(message, private_key)
valid = verify(message, signature, public_key)

print("Public key:", public_key)
print("Private key:", private_key)
print("Message:", message)
print("Signature:", signature)
print("Signature valid?", valid)
  



from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 1. Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# 2. Prepare the message
message = b"Important message to be signed!"

# 3. Sign the message
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Signature (hex):", signature.hex())

# 4. Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("The signature is valid.")
except Exception:
    print("The signature is invalid.")
