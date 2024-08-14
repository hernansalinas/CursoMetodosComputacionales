# !usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def presion(profundidad):
  presion_inicial=101325
  return presion_inicial + 1000 * 9.81 * profundidad

profundidad_maxima = 30
presion_inicial = 101325  # Presión inicial en Pa (presión atmosférica al nivel del mar)

# EJE X
profundidades = np.linspace(0, profundidad_maxima)  # Valores de profundidad
#EJE Y
presiones = presion(profundidades)  # Calcular las presiones correspondientes


plt.plot(profundidades, presiones)
plt.xlabel('Profundidad [m]', fontsize=14)
plt.ylabel('Presión [Pa]', fontsize=14)
plt.title('Variación de Presión con la Profundidad', fontsize=14)
plt.grid(True)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Calcular el número de atmósferas a la profundidad máxima
num_atmosferas = presiones[-1] / presion_inicial # [-1] nos indica que es el ultimo valor de las presiones
                                                # Y lo comvertimos en las unidades de atm
plt.text(profundidad_maxima, presiones[-1], f'{num_atmosferas:.1f} atm',
         fontsize=14, ha='right')

plt.savefig('actividad_02_graf.png')
plt.show()
