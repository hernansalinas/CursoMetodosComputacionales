def factorial(number):
	#La funcion busca el factorial de un numero n
    if number == 0:#0!=1
        return 1

    return number * factorial(number - 1)#n!=n(n-1)!


n=factorial(int(input('Dame un numero para saber su factorial: ')))
print(n)
