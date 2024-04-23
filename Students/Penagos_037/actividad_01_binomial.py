#!usr/bin/env python
def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r

def coef_binomial(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

n=int(input("Ingrese n\n"))
k=int(input("Ingrese k\n"))

print(coef_binomial(n,k))
