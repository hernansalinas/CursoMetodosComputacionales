#!usr/bin/env python 

def doble_factorial(n):

  if (type(n) == float) or (type(n) == str) or (n<0):
    print("El número debe ser positivo y entero ")
    return None

  else:
    if n == 0:
      return 1
    else:
      mul = 1
      for i in range(n,1,-2):
        mul *= i
  return mul

print(doble_factorial("as"))
