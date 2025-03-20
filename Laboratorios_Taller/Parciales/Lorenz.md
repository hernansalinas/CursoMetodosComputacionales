# Lorenz


El modelo de Lorenz es un sistema de ecuaciones diferenciales introducido por Edward Lorenz en 1963 para describir la convección atmosférica de manera simplificada. Este modelo captura la dinámica de un fluido en movimiento donde el calentamiento desde abajo y el enfriamiento desde arriba generan corrientes convectivas. A pesar de su simplicidad, el sistema exhibe un comportamiento caótico, con trayectorias que, aunque determinadas por ecuaciones bien definidas, son altamente sensibles a pequeñas variaciones en las condiciones iniciales.  

El sistema de Lorenz está descrito por las siguientes ecuaciones diferenciales:  

$$
\frac{dx}{dt} = \sigma (y - x)
$$

$$
\frac{dy}{dt} = x (\rho - z) - y
$$

$$
\frac{dz}{dt} = xy - \beta z
$$

donde:  
- $x$ representa la velocidad de convección del fluido,  
- $y$ está relacionado con la diferencia de temperatura entre las corrientes ascendentes y descendentes,  
- $z$ mide la variación vertical de la temperatura,  
- $\sigma$, $\rho$ y $\beta$ son parámetros adimensionales que dependen de las propiedades físicas del sistema.  

Para este problema, se considerarán los valores clásicos:  

- $\sigma = 10$  
- $\rho = 28$  
- $\beta = 8/3$  


* **Resuelva numéricamente el sistema de Lorenz** en el intervalo de tiempo $t \in [0,50]$, usando como condiciones iniciales $(x_0, y_0, z_0) = (1.0, 1.0, 1.0)$.  Grafique $x(t)$, $y(t)$ y $z(t)$

* **Analice la sensibilidad a las condiciones iniciales** realizando una segunda simulación con $(x_0, y_0, z_0) = (1.001, 1.0, 1.0)$. Compare la evolución de ambas soluciones en función del tiempo y determine si la diferencia entre ellas crece de manera exponencial.  

* **Represente el sistema en el espacio de fase** graficando los planos de fase $(x, y)$, $(x, z)$ y $(y, z)$. Interprete la estructura de las trayectorias y su relación con el comportamiento caótico del sistema.

