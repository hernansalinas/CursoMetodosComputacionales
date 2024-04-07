
def binomial(n,k):
    '''
    Esta función retorna el coeficiente binomial de n y k.
    '''
    def fact(a):
        if a==0:
            return 1
        else:
            fa=1
            for i in range(1,a+1):
                fa*=i
            return fa
    return fact(n)/(fact(k)*fact(n-k))

n=int(input('Ingrese un entero: '))
k=int(input('Ingrese otro entero: '))
print(f'El coeficiente binomial de {n} y {k} es: {binomial(n,k)}')
