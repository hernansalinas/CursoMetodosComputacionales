def serie_de_lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    
    a=2
    b=1
    count=2
    while count<=n:
        c=a+b
        a=b
        b=c
        count=count+1
    return c


serie_de_lucas(5)


