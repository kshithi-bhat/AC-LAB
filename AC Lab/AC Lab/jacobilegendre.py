def jacobi(a, n):
    """Compute the Jacobi symbol (a|n) for odd n > 0."""
    assert n > 0 and n % 2 == 1, "n must be positive and odd"
    
    a = a % n
    t = 1
    while a != 0:
        # Remove factors of 2
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        # Swap and apply quadratic reciprocity
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    
    return t if n == 1 else 0

def is_prime(p):
    """Check if p is prime using trial division."""
    if p <= 1:
        return False
    if p <= 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def legendre(a, p):
    """Compute the Legendre symbol (a|p) for prime p."""
    if p == 2:
        return 0 if a % 2 == 0 else 1
    if not is_prime(p) or p % 2 == 0:
        raise ValueError("p must be an odd prime or 2")
    return jacobi(a, p)





# def is_prime(p):
#     """Check if p is prime using trial division."""
#     if p <= 1:
#         return False
#     if p <= 3:
#         return True
#     if p % 2 == 0 or p % 3 == 0:
#         return False
#     i = 5
#     w = 2
#     while i * i <= p:
#         if p % i == 0:
#             return False
#         i += w
#         w = 6 - w
#     return True

# def legendre(a, p):
#     """Compute the Legendre symbol (a|p) using Euler's criterion."""
#     if p == 2:
#         return 0 if a % 2 == 0 else 1
#     if not is_prime(p) or p % 2 == 0:
#         raise ValueError("p must be an odd prime or 2")
    
#     a_mod_p = a % p
#     if a_mod_p == 0:
#         return 0
    
#     exponent = (p - 1) // 2
#     result = pow(a_mod_p, exponent, p)
#     return 1 if result == 1 else -1

# def main():
#     # User-defined values
#     a = 5
#     p = 13

#     try:
#         print(f"Legendre({a}|{p}) = {legendre(a, p)}")
#     except Exception as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     main()




def jacobi(a, n):
    """Compute the Jacobi symbol (a|n) for odd n > 0."""
    assert n > 0 and n % 2 == 1, "n must be positive and odd"
    
    a = a % n
    t = 1
    while a != 0:
        # Remove factors of 2
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        # Swap and apply quadratic reciprocity
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    
    return t if n == 1 else 0

def is_prime(p):
    """Check if p is prime using trial division."""
    if p <= 1:
        return False
    if p <= 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def legendre(a, p):
    """Compute the Legendre symbol (a|p) for prime p."""
    if p == 2:
        return 0 if a % 2 == 0 else 1
    if not is_prime(p) or p % 2 == 0:
        raise ValueError("p must be an odd prime or 2")
    return jacobi(a, p)

def main():
    # User-defined values
    a_jacobi = 5
    n_jacobi = 21  # Must be odd and positive

    a_legendre = 5
    p_legendre = 13  # Must be an odd prime
    
    try:
        print(f"Jacobi({a_jacobi}|{n_jacobi}) = {jacobi(a_jacobi, n_jacobi)}")
    except AssertionError as e:
        print(f"Jacobi error: {e}")
    
    try:
        print(f"Legendre({a_legendre}|{p_legendre}) = {legendre(a_legendre, p_legendre)}")
    except ValueError as e:
        print(f"Legendre error: {e}")

if __name__ == "__main__":
    main()

