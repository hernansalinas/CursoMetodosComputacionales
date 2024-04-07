def doble_factorial(n):
    s=n
    while(n>2):
        n=n-2
        s=s*n
    return(s)
n=5
r= doble_factorial(n)
print("El doble factorial de",n, "es", r)
n=6
r= doble_factorial(n)
print("El doble factorial de",n, "es", r)
n=8
r= doble_factorial(n)
print("El doble factorial de",n, "es", r)