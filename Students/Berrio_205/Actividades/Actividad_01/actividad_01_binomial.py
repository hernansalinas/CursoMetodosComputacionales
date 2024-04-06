n = eval(input('Ingrese el tamaño del conjunto por favor:'))
k = eval(input('Ingrese el tamaño del subconjunto por favor:'))

def factorial(n):
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
            n -= 1
        return num

def binomial(n,k):
    bin = int(factorial(n)/(factorial(k)*factorial(n-k)))
    return bin

print('Para un conjuto con', n, 'elementos, dado un subconjunto de tamaño', k, ', el coeficiente binomial es:', binomial(n,k))
