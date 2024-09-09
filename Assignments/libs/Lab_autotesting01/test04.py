config_ = add_configurations()

config_.append_("testVariable.test_Equalint","Definir x como un numero entero", "x", False,"Recuerde definir el tipo adecuado empleando el metodo int")
config_.append_("testVariable.test_Equalfloat","Defiir y como una variable tipo float", "y", False,"Recuerde definir el tipo adecuado empleando el metodo float")
config_.append_("testVariable.test_Equalstring","Definir z como un string", "z", False,"Recuerde definir el tipo adecuado emplando dobles o simples comillas")
config_.append_("testVariable.test_Equalfunctions","Definir mul_lambda como una funcion", "mul_lambda", False,"Recuerde definir la funcion")
config_.append_("testVariable.test_Equalfunctions","Definir mul_int como una funcion", "mul_int", False,"Recuerde definir la funcion")
config_.append_("testVariable.test_Equalcomplex","Definir w como un número complejo", "w", False,"Recuerde definir el tipo adecuado")
config_.append_("testVariable.test_Equalfloat","Determinar la parte imaginiaria de w", "w_img", False,"Recuerde definir el tipo adecuado")
config_.append_("testVariable.test_Equalfloat","Determinar la parte real de w", "w_real", False,"Recuerde definir el tipo adecuado")
config_.append_("testVariable.test_Equalcomplex","Calcular el complejo conjugado de w", "w_con", False,"Recuerde definir el tipo adecuado")


config_.append_("testVariable.test_Equallist","Definir una lista L", "L", True,"Recuerde definir el tipo adecuado ")


#Operaciones sobre las variables definidas
try:
  config_.append_variables_values("testOneValuesVariables.test_Expectedvaluevalue",\
                          "La longitud de lista debe ser 9 ", \
                          9,\
                          len(L),\
                          "L",
                          True)

  #Comparacion con el resultado de una variable
  config_.append_function_values("testOneValuesFunction.test_Expectedvaluevalue",\
                          "Invierta la lista L", \
                          list(reversed(L)),\
                          ("L_reverse",[]),\
                          True)



  config_.append_function_values("testOneValuesFunction.test_Expectedvaluevalue",\
                          "Determine los valores impares de la lista", \
                          L[1::2],\
                          ("L_imp",[]),\
                          False)


  config_.append_function_values("testOneValuesFunction.test_Expectedvaluevalue",\
                          "Determinar los valores pares de la lista", \
                          L[0::2],\
                          ("L_par",[]),\
                          False)


  runTest_v1(config_)

except:
  print("L no esta definida")
