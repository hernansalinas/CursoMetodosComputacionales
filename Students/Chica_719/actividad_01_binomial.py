def factorial1(n):

  if n<0:
    return("el número no puede ser negativo")
  elif type(n)==float:
    return("el número no puede ser real")
  else:
    f=1
    for i in range(n):
      f*=i+1
    return(f)
n=int(input("Escribe el numero total de elementos del conjunto: "))
k=int(input("Escribe el numero de elementos que deseas elegir de ese conjunto: "))
def binomial (n,k):
  x=factorial1(n)
  y=factorial1(k)
  z=n-k
  h=factorial1(z)
  l=x/((h)*y)
  print("El número de formas diferentes en que se pueden seleccionar de",k,"elementos de un conjunto de",n,"elementos es:",l)
  
binomial(n,k)