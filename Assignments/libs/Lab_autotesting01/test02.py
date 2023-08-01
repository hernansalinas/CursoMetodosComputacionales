config_ = add_configurations()


#mul_lambda_testing_=lambda x, y: x*y
# config_.append_function("testOneOneFunction.test_Equalfunctions",\
#                         "Crear una funcion que multiple dos numeros", \
#                         ("mul_lambda",[5,10]),\
#                         ("mul_lambda_testing_",[5,10]) ,\
#                         False, "Esto es un ayuda")

config_.append_function_values("testOneValuesFunction.test_Expectedvalue",\
                        "Crear una funcion que multiplique dos números", \
                        -1/2*2/5,\
                        ("mul_lambda",[-1/2,2/5]) ,\
                        False)



config_.append_function_values("testOneValuesFunction.test_Expectedvalue",\
                        "Crear una funcion que sume dos números", \
                        -1+2/5,\
                        ("sum_int",[-1,2/5]) ,\
                        False)
runTest_v1(config_)
