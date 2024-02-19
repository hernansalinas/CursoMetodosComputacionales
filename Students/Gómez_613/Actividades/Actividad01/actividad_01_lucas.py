def lucas(n):
    n=n-1
    l=[2,1]
    for i in range(2,n+1):
        luc=l[i-1]+l[i-2]
        l.append(luc)
    return l[n]

n=int(input('Ingrese la posición del número de Lucas que quiera: '))
print(lucas(n))
