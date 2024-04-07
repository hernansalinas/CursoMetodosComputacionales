#!/usr/bin/env python
# coding: utf-8
# %%

# %%


def doble_factorial(n):
    if n<=0:
        return 1
    else:
        return n* doble_factorial(n-2)
    
n = int(input("ingrese el número del cual se desea conocer su doble factorial: "))
print("El doble factorial de ",n, "es: ", doble_factorial(n))

