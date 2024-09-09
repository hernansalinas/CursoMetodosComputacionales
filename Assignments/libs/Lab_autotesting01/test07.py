import numpy as np
config_ = add_configurations()

config_.append_("testVariable.test_Equaldictionary","Definir una variable dicc tipo diccionario", "dicc", False,"Recuerde definir el tipo adecuado")
#Operaciones sobre las variables definidas

try:
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "la longitud del diccionario debe ser 5 ", \
                          5,\
                          len(dicc),\
                          "dicc",
                          True)


  runTest_v1(config_)

#Comparacion con el resultado de una variable
except:
  print("Las variable no han sido definidas")
  runTest_v1(config_)