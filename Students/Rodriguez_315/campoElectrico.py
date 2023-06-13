#Convirtamos esto en un programa ejecutable
import numpy as np
from scipy.misc import derivative
z = np.linspace(0,0.002,100)
R = 0.1E-3
kq=1
select = input('Seleccione campo o anillo')
def potencial (z,R,kq,select):
  if (select=='anillo'): #Vectorize nos permite evaluar el if para un array
    V = z*kq/np.sqrt(z**2+R**2)
  elif(select=='disco'):
    V = (2*kq/R**2)*(np.sqrt(z**2 + R**2)-z)
  else:
    print('error: seleccione anillo o disco')
    V = None
  return V
#potencial(z,R,kq,'disco')
try:
  derivative1 = np.vectorize(derivative,excluded =['args'] ) #Parámetros adicionales diferentes de z
  gradiente3 = derivative1(potencial,z,dx=1e-6,args=(R,kq,'disco'))
  campoElectrico = -gradiente3
  np.savetxt('campo_electrico111.txt',campoElectrico)

except:
  print('Error: anillo o disco')