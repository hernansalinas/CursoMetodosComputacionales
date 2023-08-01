config_ = add_configurations()

config_ = add_configurations()

config_.append_("testVariable.test_Equalcomplex","Definir w como un número complejo", "w", False,"Recuerde definir el tipo adecuado")
try :
  config_.append_function_values("testOneValuesFunction.test_Expectedvaluevalue",\
                          "Determinar la parte real de w", \
                          w.real,\
                          ("w_real",[]),\
                          True)

  config_.append_function_values("testOneValuesFunction.test_Expectedvaluevalue",\
                          "Determinar la parte imaginaria  de w", \
                          w.imag,\
                          ("w_img",[]),\
                          True)

  config_.append_function_values("testOneValuesFunction.test_Expectedvaluevalue",\
                          "Determinar el conjugado de w", \
                          w.conjugate(),\
                          ("w_con",[]),\
                          True)
except:
  print("Variable w is not define")
# #Construir igual valor
# config_.append_function_values("testOneValuesFunction.test_Expectedvalue",\
#                         "Crear una funcion que multiplique dos números", \
#                         5/2*2/5,\
#                         ("mul_lambda",[-1,2/5]) ,\
#                         True)



# config_.append_function_values("testOneValuesFunction.test_Expectedvalue",\
#                         "Crear una funcion que sume dos números", \
#                         -1+2/5,\
#                         ("sum_int",[-1,2/5]) ,\
#                         False)
runTest_v1(config_)
