import numpy as np
config_ = add_configurations()

config_.append_("testVariable.test_EqualSet","Definir una variable D tipo set", "D", False,"Recuerde definir el tipo adecuado")
config_.append_("testVariable.test_EqualSet","Definir una variable E tipo set", "E", False,"Recuerde definir el tipo adecuado")
config_.append_("testVariable.test_EqualSet","Definir una variable U tipo set", "U", False,"Recuerde definir el tipo adecuado")
config_.append_("testVariable.test_EqualSet","Definir una variable I tipo set", "I", False,"Recuerde definir el tipo adecuado")
#Operaciones sobre las variables definidas

try:
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "La longitud de la tupla debe ser 5 ", \
                          7,\
                          len(D),\
                          "D",
                          True)


  B1={1,-1/2,1/6,0,-1/30,0,1/42,0,-1/30,0,5/66}
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "10 primeros números de Bernulli", \
                          B1,\
                          D,\
                          "D",
                          True)

  E1=set(np.arange(1,20,1))
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "20 primeros numeros naturales ", \
                            E1,\
                            E,\
                            "E",\
                            True)

  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                              "union ", \
                              B1.union(E1),\
                              U,\
                              "U",\
                              True)



  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Calcule la interseccion ", \
                            B1.intersection(E1),\
                            I,\
                            "I",\
                            True)



  runTest_v1(config_)

#Comparacion con el resultado de una variable
except:
  print("Las variable no han sido definidas")
  runTest_v1(config_)