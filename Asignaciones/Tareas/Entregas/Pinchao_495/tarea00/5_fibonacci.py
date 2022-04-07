def fibonacci(n):
	#El ciclo se puede repetir tanto que a veces no puede dar el resultado
    if n == 0 or n == 1:
        return 1
    #fn=f(n-1)+f(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Escribe un entero: '))

print(fibonacci(n))
