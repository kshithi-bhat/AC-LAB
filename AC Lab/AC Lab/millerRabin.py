def findKandM(N):
    k = 1
    
    while((N-1)%(2**k)==0):
        k+=1
    k-=1
    m = (N-1)//2**k

    return k,m

def checkPrime(a, m, N):
    b = (a**m)%N
    
    if b == 1 or b == N-1:
        print("Probably Prime")
        return
    
    for _ in range(k-1):
        b = (b**2)%N
        if b == N-1:
            print("Probably Prime")
            return
    
    print("Composite")


N = int(input("Enter the value of N: "))

k, m = findKandM(N)
a = 2

checkPrime(a, m, N)
