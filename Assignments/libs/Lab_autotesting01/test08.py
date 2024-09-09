import numpy as np
config_ = add_configurations()

# Una forma de hacer el test
#Puede ser consultada a ataves de una pi para no exponerla a los
#estudiantes
def pi_number_expected(k):
  val=0
  gg=[]
  for i in range(0,k):
    den = (2*i+1)    
    f = 1/den
    val = val + (-1)**i *f    
  return 4*val

config_.append_function("testOneOneFunction.test_Equalfunctions",\
                      "Crear una funcion que calcule el numero pi", \
                      ("pi_number_expected",[1000]),\
                      ("pi_number",[1000]) ,\
                      True, "")

config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "Prueba para valores negativos ", \
                          type("a"),\
                          type(pi_number(-1)),\
                          "pi_number",\
                          True)

# Otra forma de hacer el test
# try:
#   config_.append_variables_values("testOneValuesVariables.test_AlmostEqual",\
#                             "Prueba de la funcion comparando con el valor esperado sin funcion", \
#                             np.pi,\
#                             pi_number(100),\
#                             "pi_number",\
#                             True,"El valor para el 10000 termino no tiene la presicion esperada")
runTest_v1(config_)



#except:
  
#  print("La funcion pi_number no esta definida")



#Segunda forma de hacer el test
# import numpy as np  







