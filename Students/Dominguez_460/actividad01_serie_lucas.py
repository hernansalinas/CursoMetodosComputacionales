#!usr/bin/env python 

def lucas(n):

  if n == 0:
    return 2
  elif n == 1:
    return 1
  elif n > 1:

    Lo = 2
    L1 = 1

    for i in range(0,n-1):
      Ln = Lo + L1
      Lo = L1
      L1 = Ln

  return L1

print(lucas(8))
