config_ = add_configurations()

config_.append_("testVariable.test_Equaltuple","Definir una tupla", "Tup", False,"Recuerde definir el tipo adecuado empleando el metodo int")

#Operaciones sobre las variables definidas
try:
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "La longitud de la tupla debe ser 5 ", \
                          5,\
                          len(Tup),\
                          "Tup",
                          True)

  

  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Los tres primeros elementos deben string ", \
                            3,\
                            sum([True if type(i)==type("a") else False for i in Tup[0:3]]),\
                            "Tup",\
                            True)


  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                            "Los dos ultimos elementos deben ser float ", \
                            2,\
                            sum([True if type(i)==type(1.0) else False for i in Tup[3:]]),\
                            "Tup",\
                            True)


  runTest_v1(config_)

#Comparacion con el resultado de una variable
except:
  print("La tupla con nombre tup no fue definida")