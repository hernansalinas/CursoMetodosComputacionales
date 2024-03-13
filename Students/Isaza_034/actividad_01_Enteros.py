#!usr/bin/sh python
"""
este programa realiza el calculo
de la división y el cociente de dos numeros ingresados por el usuario
input: a, b float
output: mensaje con el cociente y el residuo"""

a=eval(input("ingrese el numero a: "))
b=eval(input("ingrese el numero b: "))

c= a/b
print(f"La division entre a y b es: {a/b}")
print(f"El residuo entre a y b es: {a%b}")
