import phe as paillier

def main():
    # Generate public and private key pair
    public_key, private_key = paillier.generate_paillier_keypair()

    # Messages to encrypt
    messages = [42, 100, 255]

    # Encryption
    encrypted_messages = []
    for message in messages:
        encrypted_msg = public_key.encrypt(message)
        encrypted_messages.append(encrypted_msg)
        print(f"Original: {message}")
        print(f"Encrypted: {encrypted_msg}")

    # Decryption
    print("\nDecryption:")
    for encrypted_msg in encrypted_messages:
        decrypted_msg = private_key.decrypt(encrypted_msg)
        print(f"Decrypted: {decrypted_msg}")

if __name__ == "__main__":
    main()