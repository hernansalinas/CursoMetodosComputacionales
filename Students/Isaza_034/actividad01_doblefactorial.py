def doble_factorial(n):

    s = n
    while(n>=2):
        n=n-2
        s=s*n
    return s

n=4
result = doble_factorial(n)
print(f"el doble factorial de {n} es {result}")


