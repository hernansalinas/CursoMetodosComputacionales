def sucesion_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:    
      return sucesion_lucas(n-1) + sucesion_lucas(n-2)

for i in range(5):
    print(sucesion_lucas(i))
