#!/usr/bin/python
def sucesion_lucas(n):
    if n==0:
        return 2
    elif(n==1):
        return 1
    elif(n>=2):
        s_0 = 2
        s_1 = 1
        s_2 = 3
        for i in range(2,n+1):
            s_2= s_0+s_1
            s_0=s_1
            s_1=s_2
        return s_2
print(sucesion_lucas(10))
n = int(input("Ingrese un numero n: "))
result = sucesion_lucas(n)
print(f"El termino {n} de la sucesión de Lucas empezando desde el 0 es: {result}")
