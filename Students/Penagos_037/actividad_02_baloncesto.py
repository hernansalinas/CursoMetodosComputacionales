#!/usr/bin/env python

import numpy as np
from math import pi
from IPython.display import HTML
from matplotlib import pyplot as plt
from celluloid import Camera



alpha=float(input("Ingrese el ángulo del tiro\n"))
v0=float(input("Ingrese la velocidad inicial\n"))

L=10 #distancia entre tirador y la base del aro
H=3 #altura del aro
r=0.5 #radio del aro de baloncesto

vx=np.cos((pi/180)*alpha)*v0
vy=np.sin((pi/180)*alpha)*v0


x = lambda t: vx*t
y = lambda t: vy*t-(1/2)*9.8*t**2


t1=(L-r)/vx
t2=(L+r)/vx
encesta = y(t1)>H and y(t2)<H

if encesta:
    print("Encestó")
else:
    print("Falló")

tf=min(t2, 2*vy/9.8)
t=np.linspace(0, tf, 100)

plt.ioff()
fig = plt.figure()
camera = Camera(fig)
for i in t:
    plt.plot(x(i),y(i), "o", color="blue")
    plt.plot([9.5,10.5], [H,H], color="red")
    camera.snap()
plt.close()
animation = camera.animate()
animation.save('animacion_baoncesto.mp4')
HTML(animation.to_html5_video())

