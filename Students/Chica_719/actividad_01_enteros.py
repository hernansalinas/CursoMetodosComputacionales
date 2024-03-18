a=int(input("Escriba el primer numero entero: "))
b=int(input("Escriba el segundo numero entero: "))
if type(a)==(int) and type(b)==(int):
  x=a/b
  y=a%b
  print("Divisiòn:",x)
  print("Residuo",y)
else:
  print("Debe ser de tipo entero")