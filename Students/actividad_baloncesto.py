# !usr/bin/env python


import json
import numpy as np
import matplotlib.pyplot as plt

import json

datos = {
    "d": 30.0,
    "theta": 20.0,
    "vo": 5.0
}

ruta_archivo = 'datos.json'

with open(ruta_archivo, 'w') as archivo:
    json.dump(datos, archivo)

def cargar_datos_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def graficar_movimiento_parabolico(datos):
    theta = np.deg2rad(datos["theta"])
    vo = datos["vo"]
    g = 9.8 #m/s^2

    t_vuelo = (vo * np.sin(theta) + np.sqrt((vo * np.sin(theta))**2 + 2 * g * 3)) / g

    tiempo = np.linspace(0, t_vuelo, num=100)

    x = vo * np.cos(theta) * tiempo
    y = vo * np.sin(theta) * tiempo - 0.5 * g * tiempo**2

    plt.plot(x, y)
    plt.xlabel('Distancia (m)')
    plt.ylabel('Altura (m)')
    plt.title('Movimiento parabólico')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ruta_archivo = 'datos.json'
    datos = cargar_datos_desde_json(ruta_archivo)
    graficar_movimiento_parabolico(datos)
