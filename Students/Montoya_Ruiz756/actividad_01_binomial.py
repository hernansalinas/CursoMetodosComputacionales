# -*- coding: utf-8 -*-
"""actividad_01_binomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kGv75_5yFplUw1ZCcXR-gHhDRgcQasNv
"""

def factorial(n):
  if type(n) == int:
    fact = 1
    if n < 0:
      mensaje = "el número no puede ser negativo"
      return mensaje
    elif n > 1:
      fact = n * factorial(n - 1) # Se calcula el factorial
    elif n == 1:
      fact = 1
    return fact
  elif type(n) == float:
    mensaje2 = "el número no puede ser real"
    return mensaje2
def binomial(n,k):
  p = n-k
  n = factorial(n)
  d = factorial(k) * factorial(p)
  binomial = n / d
  return binomial
print("Este es un scirpt que calcula el coeficiente binomial de n y k")
n = eval(input("ingrese el número n "))
k = eval(input("ingrese el número k "))
r = binomial(n,k)
print(f"El coeficiente binomial de n y k es {r}")
