#!usr/bin/sh python


"""
Este programa realiza el cálculo de la división y el cociente de dos números ingresados por el usuario
Input: a, b float
output: Mensaje con el cociente y el residuo
"""
print("-----------------------------------------------------------------------")
print("Este programa cálcula el cociente y el residuo dados dos numeros a y b")
print("-----------------------------------------------------------------------")

a = eval(input("Ingrese el número a: "))
b = eval(input("Ingrese el número b: "))

x = a/b
y = a%b

print(f"La divisón entre {a} y {b} es: {x}")
print(f"El residuo entre {a} y {b} es: {y}")


