n = eval(input('Ingrese un número por favor'))

def doblefactorial(n):
    if type(n) == float:
        return "El número debe ser entero"
    if n < 0:
        return "el número no puede ser negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        num = 1
        while n > 1:
            num *= n
            n -= 2
        return num

print('el resultado del doble factorial es:', doblefactorial(n))
