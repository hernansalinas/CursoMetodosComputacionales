#!/usr/bin/python

"""
Este programa realiza el doble factorial de un numero ingresado por el usuario
Input: n - int
output: Mensaje con el doble factorial de n
"""
print("-----------------------------------------------------------------------")
print("Este programa cálcula el doble factorial de un numero n")
print("-----------------------------------------------------------------------")
def doble_factorial(n):
    s = n
    while(n>2):
        n=n-2
        s=s*n
    return s
n = int(input("Ingrese un numero n: "))
result = doble_factorial(n)
print(f"El doble factorial de {n} es: {result}")