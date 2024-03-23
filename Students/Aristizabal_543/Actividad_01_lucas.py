#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def lucas(n):
    a = 2
    b = 1
    c=0
    for i in range(n):
        
        c = b + a
        a = b
        b = c
        
    return b

n = int(input(("Ingrese el numero de elementos que desea conocer de la sucesión de lucas: ")))

for i in range(n):
    print(lucas(i))

