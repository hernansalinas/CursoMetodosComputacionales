# Ejercicio 3
def lucas(n):
    l=[2,1]
    while True:
        if len(l)>=n:
            break
        l.append(l[-1]+l[-2])
    return l[:n]

n=int(input("Ingrese n:\n"))
print(lucas(n))