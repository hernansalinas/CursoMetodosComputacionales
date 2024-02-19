def binomial(n,k):
    def fact(a):
        if a==0:
            return 1
        else:
            fa=1
            for i in range(1,a+1):
                fa*=i
            return fa
    return fact(n)/(fact(k)*fact(n-k))

n=int(input('Ingrese un n: '))
k=int(input('Ingrese un k: '))
print(binomial(n,k))