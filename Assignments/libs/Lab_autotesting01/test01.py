config_ = add_configurations()
config_.append_("testVariable.test_Equalint","Definir x como un numero entero", "x", False,"Recuerde definir el tipo adecuado empleando el metodo int")
config_.append_("testVariable.test_Equalfloat","Defiir y como una variable tipo float", "y", False,"Recuerde definir el tipo adecuado empleando el metodo float")
config_.append_("testVariable.test_Equalstring","Definir z como un string", "z", False,"Recuerde definir el tipo adecuado emplando dobles o simples comillas")
runTest_v1(config_)

