# Oscilador forzado de van der Pol

El oscilador de van der Pol forzado es un sistema dinámico no lineal descrito por la ecuación diferencial de segundo orden:  

$$
\frac{d^2x}{dt^2} - \mu (1 - x^2) \frac{dx}{dt} + x = A\sin(\omega t)
$$

Para $\mu = 0$, la ecuación se reduce a un oscilador armónico simple, mientras que para valores positivos de $\mu$, el sistema presenta oscilaciones autoexcitadas, conocidas como **oscilaciones límite**.  

Considere el caso con $\mu = 2$, $A = 1$, $\omega = 1$ y las condiciones iniciales:  

$$
x(0) = 1, \quad \dot{x}(0) = 0
$$

en el intervalo de tiempo $t \in [0, 10]$.  


* **Implemente la solución numérica utilizando el método de Euler explícito** con un tamaño de paso $h = 0.01$. Represente la evolución temporal de $x(t)$ y $\dot{x}(t)$.  


* **Resuelva nuevamente el sistema usando el método de Runge-Kutta de cuarto orden** (`solve_ivp`) con el mismo tamaño de paso.  

* **Compare los resultados obtenidos con ambos métodos** mediante gráficas de las soluciones y del espacio de fase $(x, \dot{x})$. Discuta las diferencias observadas en precisión y estabilidad entre los métodos.  

* Finalmente, varie $\mu$ para $0\leq \mu \leq 4$, encuentre la solución de $x(t)$ y grafique el espacio de fase. Cuál es el efecto de $\mu$ sobre el sistema?

---
## Método de Euler
Recordando que

$$
\frac{dy}{dx} = f(x,y)
$$

luego,
$$x_{n+1} = x_n + h$$
$$y_{n+1} = y_n + h * f(x_n, y_n)$$
