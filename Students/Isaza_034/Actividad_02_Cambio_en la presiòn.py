import numpy as np
import matplotlib as plt

c,g,pa = 997, 9.8, 1013
f = lambda y:pa + c*g*y

X_ = np.linspace(0, 1, 10)
Y_ = f(X_)

plt.plot(X_, Y_, "o-", label="cambio de presiòn")
plt.xlabel("profundidad_(m)", fontsize=20)
plt.ylabel("Presiòn_(pa)", fontsize=20)
plt.title("Cambio en la presiòn", fontsize=16)


