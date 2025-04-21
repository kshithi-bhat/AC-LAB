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
