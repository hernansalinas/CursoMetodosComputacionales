import sys
import numpy as np
from sympy import sympify,symbols

#area de un trapecio(metodo simple)
def area(f,a,b):
    x = symbols('x')
    return ((b-a)/2)*(f.subs(x,a)+f.subs(x,b))


def integral_trapz(f, a, b, N):
    x = symbols('x')
    suma =0
    suma2 =0
    valores_x = np.linspace(a,b,N)

    for i in range(0,len(valores_x)-1):

        suma += area(f,valores_x[i],valores_x[i+1])
        
    print(N)    
    return suma

if __name__ == "__main__":
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Uso: python integral.py <funcion> <a> <b> < N (opcional)>")
    else:
        if len(sys.argv) == 4:
            N=10
        if len(sys.argv) == 5:
            N=int(sys.argv[4])
            
            
        # Obtener la función, a y b desde los argumentos de la línea de comandos
        funcion_str = sys.argv[1]
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        x = symbols('x')

        # Convertir la cadena de función en una función de Python utilizando sympify
        funcion = sympify(funcion_str)

        # Llamar a la función integral_trapz para calcular la integral
        resultado = integral_trapz(funcion, a, b, N)
        print("Resultado de la integral:", resultado)
