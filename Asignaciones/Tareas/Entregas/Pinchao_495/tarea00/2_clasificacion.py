import	numpy as np

def clase_numero(a,b):
	div_a=[i for i in range(1,a+1) if a%i==0 ]
	div_b=[i for i in range(1,b+1) if b%i==0 ]

	def es_primo(numero):
		contador = 0
		
		for i in range(1,numero+1):
			if i==1 or i ==numero:
				continue
			if numero %i == 0:
				contador +=1
		if contador == 0:
			return True
		else:
			return False

	c=np.sum(div_a)
	d=np.sum(div_b)

	if c-a>a:
		print(f'{a} es un numero defectivo')
	if c>a:
		print(f'{a} es un numero abundante')
	if c-a==a:
		print(f'{a} es un numero perfecto')

	if es_primo(a):
		print(f'{a} es primo')
	else:
		print(f'{a} no es primo')


	if d-b>b:
		print(f'{b} es un numero defectivo')
	if d>b:
		print(f'{b} es un numero abundante')
	if d-b==b:
		print(f'{b} es un numero perfecto')

	if es_primo(b):
		print(f'{b} es primo')
	else:
		print(f'{b} no es primo')


	if c==d and d==c:
		print(f'{a} y {b} son numeros amigos')
	


num_a=int(input('Dame el primer numero: '))
num_b=int(input('Dame el segundo numero: '))
clase_numero(num_a,num_b)