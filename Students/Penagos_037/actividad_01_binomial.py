# Ejercicio 4
def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r

def coef_binomial(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(coef_binomial(5,3))