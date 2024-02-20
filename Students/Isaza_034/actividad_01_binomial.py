#!usr/bin
def factorial(n):
    producto=1
    for i in range(2, n+1):
        producto = producto * i
    return producto

def binomial(n, i):
    return factorial(n) / (factorial(i)*factorial(n-i))

binomial(5,3)   