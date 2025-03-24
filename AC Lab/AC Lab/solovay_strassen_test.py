def jacobi(a, n):
    if a == 0: return 0
    r, t = 1, 0
    while a:
        while not a & 1: a >>= 1; n8 = n & 7; r = -r if n8 == 3 or n8 == 5 else r
        a, n = n, a; r = -r if a & 3 == 3 and n & 3 == 3 else r; a %= n
    return r if n == 1 else 0

def prime_test(n, k=5):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for _ in range(k):
        a = __import__('random').randint(2, n-1)
        x = pow(a, (n-1)//2, n)
        j = jacobi(a, n) % n
        if x != j and x != (j + n) % n: return False
    return True

n = int(input("n: "))
print(f"{'Prime' if prime_test(n) else 'Composite'}")