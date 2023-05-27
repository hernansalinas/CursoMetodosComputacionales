import sys
import numpy as np

#De manera general
def integral_trapecio(f,a,b,N=100):
  #funcion1 = lambda x: eval(f)
  #f = funcion1
  h = (b-a)/N
  x = np.linspace(a,b,N+1)
  A = (f(x[0])+f(x[-1]))*0.5*h + f(x[1:-1]).sum()*h
  return A

error = len(sys.argv)
if error == 4:
    func = str(sys.argv[1])
    f = lambda x: eval(func)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    print(integral_trapecio(f,a,b))
else:
   print('no ha ingresado los argumentos necesarios.')
