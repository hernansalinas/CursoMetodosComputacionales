# -*- coding: utf-8 -*-
"""actividad_01_lucas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N-MYzrXwe_ZG6PV1ikgD-fmuH1_3MoRg
"""
"""

Esta función devuelve el número que está en la posición deseada por el usuario (n).

"""
def lucas(n):
  if n==0:
    return 2
  if n== 1:
    return 1

  return lucas(n-1)+lucas(n-2)

lucas(5)

