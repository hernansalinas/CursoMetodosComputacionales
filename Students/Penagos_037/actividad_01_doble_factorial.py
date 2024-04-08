# Ejercicio 2
def doble_factorial(n):
    r=1
    for i in range(1,n+1):
        if i%2==n%2:
            r*=i
    return r

n=int(input("Ingrese n\n"))
print(doble_factorial(n))