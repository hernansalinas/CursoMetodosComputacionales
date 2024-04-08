#!usr/bin/env python 

def binomial(n, k):

  while n >= k:

    if n == k:
      return 1

    else:
      # Factorial de k
      if k == 0:
          fack = 1
      else:
          fack = 1
          for i in range(k, 1, -1):
              fack *= i

      # Factorial de n
      if n == 0:
          facn = 1
      else:
          facn = 1
          for i in range(n, 1, -1):
              facn *= i

      # Factorial de n-k
      p = n - k
      if p == 0:
          facp = 1
      else:
          facp = 1
          for i in range(p, 1, -1):
              facp *= i

      # Calcula la fraccion
      bino = int((facn) / ((fack) * (facp)))

    return f"El coeficiente binomial es: {bino}"

    if n<k:
      return None

print(binomial(5,3))
