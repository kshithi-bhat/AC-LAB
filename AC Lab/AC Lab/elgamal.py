def inverse(a, n):
    b = 2
    while((a*b)%n!=1):
        b+=1
    return b
def encryption(M, e1 , e2, p):
    r = 4
    c1 = pow(e1,r,p)
    c2 = (M*(e2**r))%p

    return c1, c2

def decryption(c1, c2, e1, e2, p):
    inv = inverse(c1**d, p)
    plaintext = (c2*inv)%p

    return plaintext

p = int(input("Enter the value of p: "))
d = int(input("Enter value of d: "))
e1 = int(input("Enter value of e1: "))
M = int(input("Enter plaintext: "))

e2 = pow(e1,d,p)

c1, c2 = encryption(M, e1, e2, p)
print(f"Encrypted c1 and c2 are: {c1, c2}")

plaintext = decryption(c1, c2, e1, e2, p)
print(f"Decrypted plaintext is: {plaintext}")

