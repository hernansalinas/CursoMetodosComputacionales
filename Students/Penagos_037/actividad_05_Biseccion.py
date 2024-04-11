from sympy import *
from IPython.display import HTML
from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np


f=lambda x: np.exp(x)-2-np.cos(np.exp(x)-2)

err=1e-7

a=-1
b=2

plt.ioff()
fig = plt.figure()
camera = Camera(fig)
X=np.linspace(a, b, 100)

c=[b, a]

for i in range(100):
    c.append((a+b)/2)
    if f(c[-1])==0:
        print(f"Solución: x={c[-1]}")
        break
    if f(a)*f(c[-1])<0:
        b=c[-1]
    elif f(b)*f(c[-1])<0:
        a=c[-1]
    if b-a<err:
        print(f"Approximación: {c[-1]}")
        break
    print(c[-1])

for i in range(2, len(c)):
    for j in range(3):
        plt.plot(X, f(X), "b-")
        plt.plot(X, [0]*len(X), "g-")
        plt.plot(c[:i:1], [0]*i, "r.")
        plt.plot([c[i-3], c[i-3]], [0, f(c[i-3])], color="orange")
        plt.plot([c[i-2], c[i-2]], [0, f(c[i-2])], color="orange")
        plt.plot([c[i-1], c[i-1]], [0, f(c[i-1])], color="orange")
        camera.snap()


plt.close()
animation = camera.animate()
animation.save('animacion_biseccion.mp4')
HTML(animation.to_html5_video())

