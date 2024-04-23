#!/usr/bin/env python
# coding: utf-8
# %%

# %%


def factorial(a):
    if a<2:return 1
    a*=factorial(a-1)
    return a
 
def binomial(n,m): 
    if m>n: 
        print ("Error: La cantidad total de elementos debe ser mayor que la cantidad de elementos a combinar.")
    else:
        num = factorial(n)
        den = factorial(m) * factorial((n-m))
        res = num/den
        return res
        
n=int(input("Intruduzca la cantidad total de elementos: "))
m=int(input("Introduzca la cantidad de elementos a combinar: "))

print("El coeficiente binomial es: ",binomial(n,m))

