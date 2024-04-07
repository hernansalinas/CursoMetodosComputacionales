#!/usr/bin/python
def doble_factorial(n):
    s=n
    while(n>2):
        n=n-2
        s=s*n
    return(s)
result=doble_factorial(9)
print(f"el doble factorial de {n} es {result}")
