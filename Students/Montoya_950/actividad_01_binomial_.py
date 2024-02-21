#!/usr/bin/python
"""
Este programa realiza el coeficiente binomial entre n y k
Input: n, k int
output: Mensaje con el coeficiente binomial
"""
print("-----------------------------------------------------------------------")
print("Este programa cálcula el coeficiente binomial")
print("-----------------------------------------------------------------------")

from itertools import combinations
n = eval(input("Ingrese el numero de elementos que tiene el conjunto, n: "))
k = eval(input("Ingrese en numero de formas de elegir elementos distintos del conjunto, k: "))
def binomial(n,k):
  if n<0 or k<0:
    return print("Error: n y k deben ser positivos")
  elif type(n)==float or type(k)==float:
    return print("Error: n y k no pueden ser flotantes")
  elif k>n:
    return print("Error: k no puede ser mayor que n")
  else:
    lista = []
    for i in range(0,n):
      lista.append(i)
      comb = list(combinations(lista,k))
      return len(comb)
print(f"El coeficiente binomial de {n} y {k} es {binomial(n,k)}")
