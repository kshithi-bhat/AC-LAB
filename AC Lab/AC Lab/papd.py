def point_operations(P, Q, a, p):
    # Extract coordinates
    x1, y1 = P
    x2, y2 = Q
    
    # Handle special cases
    if P == (0, 0): return Q  # P is the identity point
    if Q == (0, 0): return P  # Q is the identity point
    if x1 == x2 and y1 != y2: return (0, 0)  # P + (-P) = O (identity point)

    # Determine operation: addition or doubling
    if P != Q:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p  # Point addition
    else:
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p  # Point doubling

    # Compute resulting point
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    
    return (x3, y3)

# Inputs for elliptic curve
a = int(input("Enter the coefficient 'a' of the curve equation: "))
b = int(input("Enter the coefficient 'b' of the curve equation: "))
p = int(input("Enter the prime modulus 'p': "))

# Input points P and Q
x1, y1 = map(int, input("Enter coordinates of point P (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of point Q (x2 y2): ").split())

P = (x1, y1)
Q = (x2, y2)

# Perform the operation
result = point_operations(P, Q, a, p)

# Output the result
print(f"Result of operation: {result}")