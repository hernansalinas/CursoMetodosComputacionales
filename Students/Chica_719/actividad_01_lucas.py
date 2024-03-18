n=int(input("Escribe el numero de lucas que deseas: "))
def numero_de_lucas(n):
  sl=0
  s=[1,3]
  if n==0:
    print(2)
  elif n==1:
    print(1)
  else:
    for i in range(1,n-1):
      sl=s[i]+s[i-1]
      s.append(sl)
    print("Esta es la secuencia del numero de lucas de",n,"en esta lista:",s)
    print(f"El numero de lucas de L({n}) =",s[i+1])

numero_de_lucas(n)