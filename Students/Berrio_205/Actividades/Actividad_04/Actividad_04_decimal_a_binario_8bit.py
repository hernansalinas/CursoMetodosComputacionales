##!/usr/bin/env python3

num = eval(input('Ingrese un número entrero que se pueda representar con 8 bits: '))

def mybin(x):   # Función que determina la representación binaria con 8 bit para un número entero positivo. 
    dig_i = ''
    
    if(x < 0 or x > 255):
        return '¡ El número debe estar comprendido entre 0 y 255 !'
    
    while(len(dig_i) < 8 and (0 <= x <= 255)):  # Condiciones de operación del código.
        r = x % 2
        dig_i += str(r)
        c = x // 2
        x = c
                 
    return dig_i[::-1]
            
print('La correspondiente representación binaria con 8 bit es: ', mybin(num))  
