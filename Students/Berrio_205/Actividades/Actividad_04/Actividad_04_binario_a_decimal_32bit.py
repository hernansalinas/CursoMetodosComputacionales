
def number32(BIN):    # Función que determina la representación decimal para un número binario 
                      # escrito en 32 bit (estándar IEEE 754 de precisión simple)
    s = int(BIN[0])
    E_2 = str(BIN[1:9])   # Clasificación de componentes (signo, exponenete y mantisa).
    M_2 = str(BIN[9:32])

    E = 0
    M1 = 0
    M2 = 0

    for i in range(len(E_2)):    # Ciclo para encontrar representación decimal del exponente. 
        E += int(E_2[i]) * 2**(len(E_2)-1-i)
        exp = E - 127
    
    M_2_d = 1 + (int(M_2)/10**len(M_2))
    M_2_m = str(M_2_d * 10**exp)          # Representación binaria del producto matisa, exponente.
    m = M_2_m.split('.')

    for j in range(len(m[0])):
        M1 += int(m[0][j]) * 2**(len(m[0])-1-j)   #Representación decimal de la parte entera de la mantisa.
    
    for l in range(len(m[1])):
        M2 += int(m[1][l]) * 2**(-l-1)   #Representación decimal de la parte fraccionaria de la mantisa.
    
    M = (-1)**s * (M1 + M2)

    return M

bin = input('Ingrese un número binario codificado en 32 bit')
number32(bin)

#proof = 01000011110100101101100000000000 = 421.6875
