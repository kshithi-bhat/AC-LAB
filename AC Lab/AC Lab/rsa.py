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



