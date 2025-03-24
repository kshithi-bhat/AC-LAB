from tinyec import registry
from tinyec.ec import Point
import secrets
import hashlib

class ECCCrypto:
    def __init__(self, curve_name='brainpoolP256r1'):
        """
        Initialize ECC cryptosystem with a specific curve
        Default: brainpoolP256r1 curve
        """
        self.curve = registry.get_curve(curve_name)

    def generate_key_pair(self):
        """
        Generate a private and public key pair
        
        Returns:
        - private_key: Random scalar
        - public_key: Point on the curve
        """
        private_key = secrets.randbelow(self.curve.field.n)
        public_key = private_key * self.curve.g
        return private_key, public_key

    def encrypt(self, public_key, message):
        """
        Encrypt a message using ECC
        
        Args:
        - public_key: Recipient's public key
        - message: Bytes to encrypt
        
        Returns:
        - C1: Ephemeral public key
        - C2: Encrypted message
        """
        # Convert message to bytes if it's a string
        if isinstance(message, str):
            message = message.encode()

        # Generate ephemeral key pair
        k = secrets.randbelow(self.curve.field.n)
        C1 = k * self.curve.g  # Ephemeral public key

        # Compute shared secret
        shared_point = k * public_key
        
        # Hash the x-coordinate of shared point
        shared_secret = hashlib.sha256(str(shared_point.x).encode()).digest()
        
        # XOR encryption
        C2 = bytes([m ^ s for m, s in zip(message, shared_secret * (len(message)//32 + 1))])
        
        return C1, C2

    def decrypt(self, private_key, C1, C2):
        """
        Decrypt an encrypted message
        
        Args:
        - private_key: Recipient's private key
        - C1: Ephemeral public key
        - C2: Encrypted message
        
        Returns:
        - Decrypted message
        """
        # Compute shared secret
        shared_point = private_key * C1
        
        # Hash the x-coordinate of shared point
        shared_secret = hashlib.sha256(str(shared_point.x).encode()).digest()
        
        # XOR decryption
        decrypted = bytes([e ^ s for e, s in zip(C2, shared_secret * (len(C2)//32 + 1))])
        
        return decrypted

def main():
    # Create ECC cryptosystem
    ecc_crypto = ECCCrypto()

    # Generate recipient's key pair
    private_key, public_key = ecc_crypto.generate_key_pair()

    # Message to encrypt
    message = "Hello, Elliptic Curve Cryptography!"

    # Encrypt
    C1, C2 = ecc_crypto.encrypt(public_key, message)

    # Decrypt
    decrypted_message = ecc_crypto.decrypt(private_key, C1, C2)

    # Print results
    print("Original Message:", message)
    print("Encrypted Message (C2):", C2)
    print("Decrypted Message:", decrypted_message.decode())

if __name__ == "__main__":
    main()
