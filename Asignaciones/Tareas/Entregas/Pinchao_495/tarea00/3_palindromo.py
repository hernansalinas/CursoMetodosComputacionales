def palindromo(numero):
	#Invierte los numeros y si el numero invertido y el numero agregado son igual es palindromo
	#Tambien funciona con palabras
	space=numero.strip()
	print(numero)
	print(space)
	numero=numero.replace(' ','')
	numero=numero.lower()
	numero_invertida=numero[::-1]
	if numero==numero_invertida:
		return True
	else:
		return False


numero =input('Escribe una numero: ')
es_palindromo=palindromo(numero)
if es_palindromo==True:
	print('Es palindromo')
else:
	print('No es palindromo')