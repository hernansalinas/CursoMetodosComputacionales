n = eval(input('Ingrese un número por favor'))

def lucas(n):
    if n == 0:
        return 2
    if n ==1 :
        return 1
    else: 
        return lucas(n-1) + lucas(n-2)

print('El número en la posición', n, 'de la sucesión de Lucas es:', lucas(n))
    
