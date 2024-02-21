
def lucas(n):
    '''
    Esta función devuelve el n-ésimo término de la serie de Lucas.
    '''
    l=[2,1]
    for i in range(2,n+1):
        luc=l[i-1]+l[i-2]
        l.append(luc)
    return l[n]

n=int(input('Ingrese la posición del número de Lucas que desea: '))
print(f'El número de Lucas que ocupa la posición {n} es: {lucas(n)}')
