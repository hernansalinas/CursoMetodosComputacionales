# dado un tetha y una velocidad inicial

import matplotlib.pylab as plt
import numpy as np
import json

#data
#data={"x":x, "y":y}
with open("input.json", "r") as f:
    data=json.load(f)
print(data)
tetha = data["tetha"]
vo = data["vo"]
d = data["d"]
print(tetha, vo, d)
x = np.linspace(0, 10, 1000)
y = np.sin(x)

np.savetxt("salida.txt", (x,y))

def cesta(vo, theta, d):
    g=9.8
    vox = vo * np.cos(tetha)
    voy = vo * np.sin(tetha)
    trayectoriaX = lambda t: (vox)* t
    trayectoriaY = lambda t: (voy)* t - (0.5*g*(t**2))
    
    tiempoX = d/vox
    
    X = np.linspace(0,trayectoriaX(tiempoX),100)
    Y = trayectoriaY(X)
    
    plt.xlabel("trayectoria en x", fontsize=20)
    plt.ylabel("trayectoria en y", fontsize =20)
    plt.plot(X,Y)
    plt.show()
    
    if trayectoriaY(tiempoX) == 3:
        return True
    else:
        return False


cesta(28.5, 3.14/6, 4)
