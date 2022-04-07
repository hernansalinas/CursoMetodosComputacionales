def palabra(palabra):
	#Determina si la letra del medio es vocal
	n=int(len(palabra)/2)
	lista=[]
	if palabra[n] in 'aeiou':
		lista.append(True)
	else:
		lista.append(False)
	
	#Busca las consonantes y vocales
	vocales=[i for i in palabra if i in 'aeiou']
	consonantes=[i for i in palabra if i not in 'aeiou']
	reverso=palabra[::-1]#Invierte la palabra
	lista.append(len(vocales))
	lista.append(len(consonantes))
	lista.append(reverso)
	print(lista)

palabra(input('Dame una palabra: '))
