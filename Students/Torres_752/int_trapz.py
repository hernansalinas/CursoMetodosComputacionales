#Programa de integrales numericas

import sys
import numpy as np
import scipy as sc
#from matplotlib import pyplot as plt



error=""" Este programa tiene la siguiente estructura de entrada de parametros:

Param1: expresion algebraica de una funcion
Param2:a , limite inferior
Param3:b , limite superior

El programa se ejecuta asi:
python Param1 Param2 Param3
"""




def integral_trapz_2(funcion,a,b, N=10): # Version vectorizada.
  
  h=(b-a)/N
  X=np.linspace(a,b,N+1)                                  

  A_t=((funcion(X[0])+funcion(X[-1]))*(h/2))+  funcion(X[1:-1]).sum()*h    

  return A_t


if len(sys.argv)!=4+1: #Agregamos +1 para contabilizar el elemento contenido en el indice 0.
    print(error)
    exit(1)

func=sys.argv[1]
a0=sys.argv[2]
b0=sys.argv[3]
N0=sys.argv[4]



f=lambda x: eval(func)
a=eval(a0)
b=eval(b0)
N=eval(N0)

print(integral_trapz_2(f,a,b,N))