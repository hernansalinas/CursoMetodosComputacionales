from sympy import *
from IPython.display import HTML
from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np


x=Symbol("x")

f=x**2-2

x0=0
x1=-1

err=1e-7

plt.ioff()
fig = plt.figure()
camera = Camera(fig)
X=np.linspace(-3, 0, 100)
Y=[f.evalf(subs={x:i}) for i in X]
plt.plot(X,Y)


for i in range(100):
    f0=f.evalf(subs={x: x0})
    f1=f.evalf(subs={x: x1})
    
    for i in range(3):
        plt.plot(X,Y, color="blue")
        plt.plot([x0, x1, x1-(x1-x0)/(f1-f0)*f1], [f0, f1, 0], color="red")
        plt.plot(X, [0]*len(X), color="green")
        camera.snap()

    for i in range(3):
        plt.plot(X,Y, color="blue")
        plt.plot([x1-(x1-x0)/(f1-f0)*f1, x1-(x1-x0)/(f1-f0)*f1], [0, f.evalf(subs={x: x1-(x1-x0)/(f1-f0)*f1})], color="red")
        plt.plot(X, [0]*len(X), color="green")
        camera.snap()
    
    a=x1
    x1=x1-(x1-x0)/(f1-f0)*f1
    x0=a
    if abs(x1-x0)<err:
        print(f"Aproximación: {x1}")
        break
    print(x1)

plt.close()
animation = camera.animate()
animation.save('animation.mp4')
HTML(animation.to_html5_video())
