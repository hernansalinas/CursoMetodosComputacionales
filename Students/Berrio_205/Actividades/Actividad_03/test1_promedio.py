
n = eval(input('Ingrese el tamaño muestral : ')) # Definición del tamaño muestral.
datos = np.zeros(n) 

for i in range(n):  # Ciclo para solicitar el ingreso de los n datos.
    dato = eval(input())  
    datos[i] = dato    # Construcción de un arreglo de numpy con los datos.

def promedio(x):   # Función que determina el promedio a un conjunto de datos (arreglo de numpy).
    prom = 0
    for i in x: 
        prom += i
    return prom / len(x)
    
print('El promedio aritmético para los datos ingresados es: ', promedio(datos))
