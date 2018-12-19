import numpy as np

# Crea una lista vacia de 'cantidadElementos' elementos.
def crearLista(cantidadElementos):
	return [None]*cantidadElementos

# Dado 	'valor' lo agrega 'cantidad' a la 'lista' 'desde' una posicion especifica.
def asignarElementosLista(desde, cantidad, valor, lista):
	for x in range(cantidad):
		lista[x + desde] = valor
		

# Busca a cual de todos los 'pps' pertenece una 'medicion' dada. Siempre eligiendo
# la mas cercana en tiempo.		
def determinarIndicePPS(indice, medicion, indiceMedicion, pps):
	indicePPS = {'indiceMedicion': indiceMedicion}

	if (indice == 0):
		indicePPS['indicePPS'] = 0
	elif (indice == len(pps)):
		indicePPS['indicePPS'] = indice - 1
	elif(abs(pps[indice] - medicion) < abs(pps[indice - 1] - medicion)):
		indicePPS['indicePPS'] = indice
	else:
		indicePPS['indicePPS'] = indice - 1
		
	return indicePPS
	
# Calcula la funcion de distribucion acumulada de los 'datos' dados y devuelve la informacion necesaria para 
# poder graficarla.
def calcularFda(datos):
	offsetOrdenados = sorted([abs(x) for x in datos])

	integral = []
	minimo = min(offsetOrdenados)
	actual = 0
	
	for valor in offsetOrdenados:
		actual += valor
		integral.append(actual)
		
	maximo = max(offsetOrdenados)
	
	integral = [maximo * x/integral[-1] for x in integral]
	
	longitudFda = len(integral)
	x = integral[:]
	y = [x/longitudFda for x in range(longitudFda)]

	return x, y