{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GrhlCVr1lS7o"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hernansalinas/autogrades/blob/main/Laboratorios_Taller/Lab03_Algoritmia_y_graficacion.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SkZguDaDeyAZ"
      },
      "source": [
        "# Laboratorio 03\n",
        "\n",
        "\n",
        "1.0 Caos numérico en un mapa logístico y errores de punto flotante (Errores de redondeo)\n",
        "\n",
        "> Un ejemplo clásico de caos,  es el comportamiento no lineal en las interaciones de un mapa logístico\n",
        "\n",
        "\\begin{equation}\n",
        "x_{n+1}=f(x_n)=rx_n(1-x_n)\n",
        "\\end{equation}\n",
        "\n",
        "> con $x\\in (0,1)$ y $r\\in(0,4)$ se pueden producir varios comportamientos sorprendentes.\n",
        "\n",
        "Para este problema, será extremadamente útil  ver sus resultados gráficamente; construya listas de números y llame la libreria matplotlib.\n",
        "\n",
        "\n",
        "> ### Problema:\n",
        "a. Programar la ecuación para el mapa logístico, y  realizar una grafica del valor de xn como funcion de n.\n",
        "\n",
        "b. Realizar pruebas para un $x_0=0.5$, con valores de r\n",
        "\n",
        "```\n",
        "  r = np.array([1.9, 2.9, 3.1, 3.5, 3.9,4.0])\n",
        "  numpoints = 100, # Numero sugerido de iteraciones\n",
        "  x0 = 0.5\n",
        "```\n",
        "\n",
        "Organizar las gráficas [multiples plot](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)\n",
        "\n",
        "\n",
        "\n",
        "c. Construye una rutina llamada logist_map en que entrada el valor de r, la condiciones inicial xi y el número de puntos determine la evolución en el punto N.  Prueba implementado las siguientes lineas.\n",
        "\n",
        "```\n",
        "Np = 1000\n",
        "xf = np.zeros(Np)\n",
        "r  = np.linspace(2.5, 4, Np)\n",
        "\n",
        "for i in range(0, Np):\n",
        "  xini = np.random.random()\n",
        "  x_i = logist_map(r = r[i], xi = xini, N = 1000)\n",
        "  xf[i] = x_i\n",
        "```\n",
        "\n",
        "\n",
        "d. Realiza un gráfico de:\n",
        "```\n",
        "  plt.plot((r-1/r), xf,  \".\", markersize = 0.5)\n",
        "```\n",
        "\n",
        "\n",
        "e. Encontrar dos formas adicionales de expresar $f(x)$, para estos valores funcionales determinar las mismas gráficas del numeral 3 para cada uno de las formas de escribir la expresión. En este caso se espera que los resultados varien. ¿A que se debe esto?. Consulta algunas fuentes para responder a la pregunta.\n",
        "\n",
        "\n",
        "Ref: https://www.youtube.com/watch?v=EOvLhZPevm0&t=104s\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#mapa logistico\n",
        "# la variable independiente es la n y la variable dependiente es la X_n, por lo tanto en el eje horizontal estara n y en el eje vertical estara X_n\n",
        "\n",
        "\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "def mapa_logistico(r,x0,n):\n",
        "    x=np.zeros(n)\n",
        "    for i in range (0,n):\n",
        "        xn=r*x0*(1-x0)\n",
        "        x[i]=x0\n",
        "        x0=xn\n",
        "    return x"
      ],
      "metadata": {
        "id": "7CzI5HwMZSzq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GkaL0-AQVQ4x"
      },
      "source": [
        "2. El mapa de Hénon es un sistema dinámico discreto en el tiempo que se define por las siguientes ecuaciones:\n",
        "\n",
        "$$x_{n+1} = 1 - ax_n^2 + y_n$$\n",
        "$$y_{n+1} = bx_n$$\n",
        "\n",
        "Donde $x_n$ y $y_n$ son las coordenadas de un punto en el plano, y $a$ y $b$ son dos parámetros que controlan el comportamiento del mapa. El mapa de Hénon es uno de los ejemplos más estudiados de sistemas dinámicos que muestran comportamiento caótico, es decir, una gran sensibilidad a las condiciones iniciales y una estructura fractal.\n",
        "\n",
        "El mapa de Hénon fue introducido por Michel Hénon como un modelo simplificado de la sección de Poincaré del modelo de Lorenz, que es otro sistema dinámico caótico que describe la convección atmosférica². Para los valores clásicos del mapa de Hénon, que son $a = 1.4$ y $b = 0.3$, un punto inicial del plano se acercará a un conjunto de puntos conocido como el atractor extraño de Hénon, o divergirá al infinito. El atractor de Hénon es una curva suave en una dirección y un conjunto de Cantor en otra.\n",
        "\n",
        "Su tarea será:\n",
        "1. Construir una gráfica de xn como función de N\n",
        "2. Construir una gráfica de yn como función de N\n",
        "3. Construir una gráfica de xn, yn.\n",
        "4. Para b=0.3, construir una curva de xn como función de a, con a entre 0, 1\n",
        "\n",
        "\n",
        "Reto, con tu codigo, reproducir los fractales mostrados en esta página https://blbadger.github.io/henon-map.html"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "def mapa_henon (a,b,x0,y0,n):\n",
        "    x=np.zeros(n)\n",
        "    y=np.zeros(n)\n",
        "    for i in range(n):\n",
        "        xn= 1 - a* (x0)**2 + y0\n",
        "        yn=b * y0\n",
        "        x[i]=x0\n",
        "        y[i]=y0\n",
        "        y0=yn\n",
        "        x0=xn\n",
        "    return x,y\n",
        "\n",
        "resultado=mapa_henon(1.4,0.3,3,3,3)\n",
        "print (resultado)\n",
        "\n",
        "\n",
        "#grafica de xn en funcion de n\n",
        "\n",
        "lista0=[]\n",
        "for i in range (0,n+1):\n",
        "  x_1=mapa_henon(a,b,x0,y0,n)\n",
        "  lista0.append(x_1)\n",
        "\n",
        "\n",
        "plt.xlabel(\"n\")\n",
        "plt.ylabel(\"x0\")\n",
        "plt.title(\"grafica de x0 en de y0\")\n",
        "plt.show\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "lU3yyE0dYy3M",
        "outputId": "05988294-a219-4e11-935c-467dcb5c5fda",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(array([   3.   ,   -8.6  , -101.644]), array([3.  , 0.9 , 0.27]))\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'n' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-58a955fa1edc>\u001b[0m in \u001b[0;36m<cell line: 23>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0mlista0\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m   \u001b[0mx_1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmapa_henon\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mx0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0my0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m   \u001b[0mlista0\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx_1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'n' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TfAf3lDVfD1d"
      },
      "source": [
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3X1VWZyEhjaM"
      },
      "source": [
        "3.0 El algoritmo de gradiente descendente permite encontrar el mínimo de funciones en espacios multidimensionales proponiendo puntos en la dirección en la que el gradiente desciende. Para el caso de una dimensión, podemos encontrar el mínimo realizando iteraciones y multiplicando su derivada en cada nuevo punto por una constante $\\alpha$\n",
        "\n",
        "\\begin{equation}\n",
        "x_{i+1}=x_i - \\alpha \\frac{\\mathrm{d}f}{\\mathrm{d}x}(x_i)\n",
        "\\end{equation}\n",
        "\n",
        "\n",
        "Ejemplo:\n",
        "\n",
        "Sea $f(\\omega) = (\\omega-1)^2$ , con $\\omega \\in \\mathbb{R} $. El minimo de esta función esta determinado por\n",
        "\\begin{equation}\n",
        "\\frac{\\mathrm{d}f}{\\mathrm{d}\\omega} = 0\n",
        "\\end{equation}\n",
        "\n",
        "\\begin{equation}\n",
        "\\omega = 1\n",
        "\\end{equation}\n",
        "\n",
        "\n",
        "Para determinar el minimo,  a través del gradiente descendente puede ser aplicada el siguiente algoritmo:\n",
        "1. Proponer un número aleatorios inicial $\\omega_i$\n",
        "2. Para descender al mínimo de la función, encontremos un  valor para el cual\n",
        "la derivada de la función descenciende, asi:\n",
        "\\begin{equation}\n",
        "\\omega_{i+1} = \\omega_{i} - \\alpha \\frac{\\mathrm{d}f(\\omega_i)}{\\mathrm{d}\\omega}\n",
        "\\end{equation}\n",
        "\n",
        "donde, $\\alpha$ es conocido como la tasa de aprendizaje del algoritmo.\n",
        "\n",
        "3. Evaluar $f(\\omega_{i+1})$\n",
        "\n",
        "4. Iterar hasta encontrar el minimo de la función\n",
        "\n",
        "\n",
        "En el caso de la funcion propuesta, asumiendo un valor de $\\alpha=1$, tenemos que:\n",
        "\n",
        "1. Supongamos que $\\omega_{0} = 2$, luego :\n",
        "2. $\\omega_{0+1} = 2 - 1 f'(\\omega_{0}) =  = 0$\n",
        "3. $f(0) = 1$\n",
        "4. $\\omega_{1+1} = 0 - 1 f'(\\omega_{1}) = 0-1(2(0-1)) =  2$\n",
        "\n",
        "El valor del $\\omega$  despues de un par de iteraciones, no es el esperado, por que no minimiza la función, se debe proponer un tasa de aprendizaje  **$\\alpha$** de tal forma que permita descender suavemente para encontrar el minimo.\n",
        "\n",
        "\n",
        "\n",
        "**Su tarea será**:\n",
        "\n",
        "1. Disenar un programa, en el que entrada la función y su derivada, definidas como funciones lambda de python, se determine el valor mínimo de esa función.\n",
        "Prueba tu algoritmo para  la función $f(x) = x^2$\n",
        "\n",
        "2. Realiza el grafico de la funcion y la derivada, especifica la leyenda de cada curva empleando el metodo legend() de matplotlib.\n",
        "  \n",
        "\n",
        "3. Analiza como se minimiza la función, gráficando de la funcion en cada punto a iterar,  como funcion del numero de iteraciones. Para dos valores diferentes de la constante alpha (prueba con $\\alpha=0.1$, $\\alpha=0.01$)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "#1\n",
        "funcion=lambda x:x**2\n",
        "derivada=lambda x:2*x\n",
        "\n",
        "def gradiente (funcion,derivada,a,w0,n):\n",
        "    w=np.zeros(n)\n",
        "    for i in range(n):\n",
        "        der= derivada(w0)\n",
        "        wn=(w0) - a *der\n",
        "        w[i]=wn\n",
        "        w0=wn\n",
        "    return wn\n",
        "\n",
        "\n",
        "#2\n",
        "resultado=gradiente(funcion,derivada,1,2,2)\n",
        "print(resultado)\n",
        "\n",
        "#grafica de la funcion\n",
        "x_p=np.linspace(-5,5,100) #x para evaluar en la funcion\n",
        "y_f=funcion(x_p) #evaluar todos los puntos en la funcion\n",
        "y_d=derivada(x_p)\n",
        "\n",
        "plt.plot(x_p,y_f,label=\"funcion\")\n",
        "plt.plot(x_p,y_d,label=\"derivada\")\n",
        "plt.ylabel(\"Y\")\n",
        "plt.xlabel(\"X\")\n",
        "plt.legend()\n",
        "plt.show\n",
        "\n",
        "#3 para este punto hay que actualizar el valor de la funcion en cada iteracion y guardarlo\n",
        "\n",
        "def gradiente (funcion,derivada,a,w0,n):\n",
        "    w=np.zeros(n)\n",
        "    f=np.zeros(n)\n",
        "    for i in range(n):\n",
        "        der= derivada(w0)\n",
        "        wn=(w0) - a *der\n",
        "        w[i]=wn\n",
        "        f[i]=funcion(w0)\n",
        "        w0=wn\n",
        "    return w,f\n",
        "\n",
        "w, f = gradiente(funcion,derivada,0.1,2,4)\n",
        "\n",
        "plt.plot(w,f,\"*--r\")\n",
        "plt.xlabel(\"X\")\n",
        "plt.ylabel(\"y\")\n",
        "plt.title(\"la funcion en cada iteracion\")\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 489
        },
        "id": "BbCVosXiGelM",
        "outputId": "b9c28e31-7ba5-4f3e-f59b-80a02876f37c"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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nu90r//rr782AOP3338vabv99tsNNzc3Iy4u7pTrTzz/id/xRYsWGYZx8n1r2bKlcezYsZLrf/zxRwMwxo8fX9I2fPhwAzCeffbZUo/dtm1bo3379qc8p8iF0FCXSBn5+vqW/P+srCwOHTpEt27dyM3NZdu2bZVSw4033ki1atVKvj/RC7Br1y4A0tLS+P3337nzzjupW7duqfue+Ov9dObPn09BQQEPPvggbm4n/5m4++67CQoK4qeffip1fUBAALfeemvJ915eXnTq1KmkjjOZNWsWdrudoUOHcujQoZKvyMhIGjVqdMqQUFmf57vvvsNutzN+/PhSrwdKvw/n8zNdtWoVqamp3HPPPaV6NkaMGEFwcHCpx3Z3dy+5xm63c+TIEYqKiujQoQNr1qw5a80XYt26dezYsYNbbrmFw4cPl7yPOTk59OrVi99//x273V7qPvfcc88pj/P315+Xl8ehQ4e45JJLAErqtdvtfPfddwwcOJAOHTqc8hhn+r068b7de++9peb+DBgwgKZNm57yO3W6Grt163bOn7XIuWioS6SMNm/ezFNPPcXChQvJzMwsdVtGRkal1PDPMHMiBB09ehQ4GYBatmx5QY+7Z88eAJo0aVKq3cvLi5iYmJLbT6hTp84pH3jVqlVjw4YNZ32eHTt2YBgGjRo1Ou3tfx9Ou5jnSUhIwM3NjebNm5/1uvP5mZ547f+s2dPTk5iYmFMe89NPP+W1115j27ZtFBYWlrRHR0eftZYLsWPHDgCGDx9+xmsyMjJKheTTPf+RI0eYMGEC06dPL5mA//f7gxmmMzMzy+13CqBp06b8+eefpdp8fHwICwsr1VatWrWS322RslLwESmD9PR0evToQVBQEM8++ywNGjTAx8eHNWvW8Nhjj53y1/X5stlsJfMt/u5MEzrPtBLrdI9Rkcpah91ux2azMXfu3NM+RkBAQLk8z/moiJ/pF198wYgRIxg0aBCPPPII4eHhuLu7M3HiRBISEi665hNO1PbKK6+ccd7QP9/Lv/funDB06FD++usvHnnkEWJjYwkICMBut9OvX78y/06XlVYZSkVR8BEpg8WLF3P48GFmzZpF9+7dS9oTExMv6nGrVat22q78f/awnK8TPRCbNm26oPud2EwxPj6+VC9GQUEBiYmJ9O7du0z1/FODBg0wDIPo6GgaN25cLo95puex2+1s2bLljMHgfH+mJ96bHTt2cMUVV5S0FxYWkpiYSJs2bUraZs6cSUxMDLNmzSrVU/X000+X6XWcaRipQYMGAAQFBZX5Z3P06FEWLFjAhAkTGD9+fEn7id6kE8LCwggKCrqo36m/v28n2rSBp1QWzfERKYMTf43+vaehoKCA995776Iet0GDBmzbto20tLSStvXr15+yJPl8hYWF0b17d6ZMmcLevXtL3Xa2XpLevXvj5eXFW2+9Veq6Tz75hIyMDAYMGFCmev5p8ODBuLu7M2HChFPqMQzjtMuoy2LQoEG4ubnx7LPPntJzceJ5z/dn2qFDB8LCwpg8eXLJ0m0wVyz9c6n/6R5zxYoVLFu2rEyv48ReO/98nvbt29OgQQNeffVVsrOzT7nf33+fzuR0tQJMmjSp1Pdubm4MGjSIH374gVWrVp3yOGf6verQoQPh4eFMnjyZ/Pz8kva5c+eydevWcvudEjkX9fiIlEHXrl2pVq0aw4cP54EHHsBms/H5559f9JDLnXfeyeuvv07fvn0ZOXIkqampTJ48mRYtWpwy5+R8vfXWW1x22WW0a9eOUaNGER0dze7du/npp5/OeD5YWFgYTzzxBBMmTKBfv35cc801xMfH895779GxY8dSE4wvRoMGDXj++ed54okn2L17N4MGDSIwMJDExERmz57NqFGjePjhhy/6eRo2bMiTTz7Jc889R7du3Rg8eDDe3t7ExcVRq1YtJk6ceN4/U09PT55//nlGjx7NFVdcwY033khiYiJTp049ZY7P1VdfzaxZs7juuusYMGAAiYmJTJ48mebNm582oJxLgwYNCAkJYfLkyQQGBuLv70/nzp2Jjo7m448/pn///rRo0YI77riD2rVrc+DAARYtWkRQUBA//PDDWR87KCiI7t278/LLL1NYWEjt2rX57bffTtuL+eKLL/Lbb7/Ro0cPRo0aRbNmzTh48CDffPMNf/7552k35vT09OSll17ijjvuoEePHtx8880ly9nr16/PQw89dMHvh0iZVPYyMhFHdLrl7EuXLjUuueQSw9fX16hVq5bx6KOPGr/++mupJbxncqbl7IZhGF988YURExNjeHl5GbGxscavv/56xuXsr7zyyin3B4ynn366VNumTZuM6667zggJCTF8fHyMJk2aGP/5z3/O+voMw1y+3rRpU8PT09OIiIgwxowZ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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "c6MylR8Nc3kT"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.9"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}