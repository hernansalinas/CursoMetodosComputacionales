# -*- coding: utf-8 -*-
"""actividad_01_doble_factorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XWXJdWUru9bAN4uRN8u_K5kWYuP-qwKz
"""

"""
Esta función cálcula el doble factorial de un número dado por el usuario (n).

"""

def doble_factorial(n):
  l = list(range(1,n+1))
  df = 1
  for i in l[-1:0:-2]:
    df *= i

  return print(df)

doble_factorial(17)