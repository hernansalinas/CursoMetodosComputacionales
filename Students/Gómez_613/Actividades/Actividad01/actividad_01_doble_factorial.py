
def doble_factorial(n):
    '''
    Esta función calcula en doble factorial de un entero n.
    '''
    if n<0:
        return 'Ingrese un número no negativo.'
    if n%2==0:
        feven=1
        for i in range(0,n/2+1):
            feven*=2*i
        return feven
    else:
        if n%2!=0:
            fodd=1 
            for j in range(1,int(((n+1)/2))+1):
                fodd*=2*j-1
            return fodd
        
n=int(input('Ingrese un entero n: '))
print(f'{n}!!={doble_factorial(n)}')
