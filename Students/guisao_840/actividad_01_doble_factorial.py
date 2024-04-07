def doble_factorial(n):
  if n%2==0:
    for i in range(2,n,2): #doble factorial cuando el numero es par
      n=n*i
    return(n)
  if n<1:  #el numero debe ser positivo
    return('el numero no puede ser negativo')

  if n>1:
    for i in range(1,n,2): #doble factorial cuando el numero es impar
       n=n*i
    return(n)


doble_factorial(10)
