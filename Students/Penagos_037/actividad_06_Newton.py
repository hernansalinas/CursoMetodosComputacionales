from sympy import *
from IPython.display import HTML
from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np


x=Symbol("x")
f=exp(x)-2-cos(exp(x)-2)
df=diff(f, x)

err=1e-7

x0=4

plt.ioff()
fig = plt.figure()
camera = Camera(fig)
X=np.linspace(-1, 4, 100)
Y=[f.evalf(subs={x:i}) for i in X]
plt.plot(X,Y)

for i in range(100):
    if f.evalf(subs={x: x0}) == 0:
        print(x0)
        break
    if abs(f.evalf(subs={x: x0})/df.evalf(subs={x: x0})) < err:
        print(f"Aproximación: {x0}")
        break
    for i in range(3):
        plt.plot([x0, x0-f.evalf(subs={x: x0})/df.evalf(subs={x: x0})],  [f.evalf(subs={x:x0}), 0], color="red")
        plt.plot(X,Y, color="blue")
        plt.plot(X, [0]*len(X), color="orange")
        camera.snap()
    x0-=f.evalf(subs={x: x0})/df.evalf(subs={x: x0})
    for i in range(3):
        plt.plot([x0,x0],  [f.evalf(subs={x: x0}), 0], color="green")
        plt.plot(X,Y, color="blue")
        plt.plot(X, [0]*len(X), color="orange")
        camera.snap()
    print(x0)

plt.close()
animation = camera.animate()
animation.save('animacion_newton.mp4')
HTML(animation.to_html5_video())

