import sys  


def integral_trapz(fun, a = eval(sys.argv[2]), b = eval(sys.argv[3]), N= eval(sys.argv[4])):
  '''ingrese la función a integrar, el punto de inicio y el punto final. Opcional ingresar el numero de trapecios que quiere realizar'''
  
  k = 0
  h = (b-a) / N
  A = 0
  
  while k < N:
    A +=  (h/2) *  (fun(a + k*h) + fun(a + (k+1)*h))
    k += 1  
    
  return A


f = lambda x: eval(sys.argv[1])

print(integral_trapz(f))