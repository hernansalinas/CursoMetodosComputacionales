# Ejercicio 2
def doble_factorial(n):
    r=1
    for i in range(1,n+1):
        if i%2==n%2:
            r*=i
    return r

print(doble_factorial(5))
print(doble_factorial(6))
print(doble_factorial(7))
print(doble_factorial(8))