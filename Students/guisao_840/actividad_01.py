#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'actividad_01_enteros.py', 'def div(a,b):\n  c=a/b\n  d=a%b\n  return(c)\n  return(d)\ndiv(6,2)\n')


# In[2]:


get_ipython().run_cell_magic('writefile', 'actividad_01_doble_factorial.py', "def doble_factorial(n):\n  if n%2==0:\n    for i in range(2,n,2): #doble factorial cuando el numero es par\n      n=n*i\n    return(n)\n  if n<1:  #el numero debe ser positivo\n    return('el numero no puede ser negativo')\n\n  if n>1:\n    for i in range(1,n,2): #doble factorial cuando el numero es impar\n       n=n*i\n    return(n)\n\n\ndoble_factorial(10)\n")


# In[3]:


get_ipython().run_cell_magic('writefile', 'actividad_01_lucas.py', 'def lucas(n):\n  l1=2 #primer termino de la sucesion\n  l2=1 #segundo termino del a sucesion\n  for i in range(0,n-1):\n    sum=l1+l2\n    l1=l2\n    l2=sum\n  return(sum)\n\nlucas(5)\n')


# In[4]:


get_ipython().run_cell_magic('writefile', 'actividad_01_binomial.py', 'def factorial(n):\n  if n>0:\n    for i in range(1,n):\n      n=n*i\n    return(n)\n\ndef binomial(n,k):\n  rest=n-k\n  bn= (factorial(n))/((factorial(k))*(factorial(rest)))\n  return bn\n\nbinomial(7,2)\n')


# In[ ]:




