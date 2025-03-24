a = int(input("Enter value of a (pvt key of user a): "))
b = int(input("Enter value of b (pvt key of user b): "))
g = int(input("Enter the value of g: "))
n = int(input("Enter the value of n: "))

pub_a = pow(g,a,n)
pub_b = pow(g,b,n)

shared_key_1 = pow(pub_a, b, n)
shared_key_2 = pow(pub_b, a, n)

print(f"{shared_key_1} and {shared_key_2}")