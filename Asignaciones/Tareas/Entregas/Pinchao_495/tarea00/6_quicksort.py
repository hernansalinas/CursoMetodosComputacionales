a_list = []

while True:
	#Pide datos que desee el usuario hasta que no reciba nada
	s = input('Introduce los numeros: ')
	if not s:
		break
	a_list.append(int(s))

def qsort(list):
	#Quicksort pivotes
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

print(qsort(a_list))

b=a_list
b.sort()
print(b)
