from bisect import bisect_left
from nucleo import *

# Realiza el apareo de 't1Mediciones' y los 'pps'
def asignarMedicionesPPS(t1Mediciones, pps):
	indices = crearLista(len(t1Mediciones))
	i = 0
	
	for indiceMedicion, medicion in enumerate(t1Mediciones):
		# Primero busca donde deberia ir ubicado esa medicion en los PPS.
		indice = bisect_left(pps, medicion)
		# Y luego determina exactamente a donde corresponde.
		indices[i] = determinarIndicePPS(indice, medicion, indiceMedicion, pps)
		i += 1	
		
	return indices
	
# Repite los 'phiNTP' para que tengan la misma cantidad de elementos que
# los phiReales.
def expandirMediciones(indices, phiReales, phiNTP):
	indices.sort(key = lambda x: (x['indicePPS']))
	
	primeraPosicion = indices[0]['indicePPS']

	phiRealesAcortada = phiReales[primeraPosicion:]	

	phiNTPExtendido = crearLista(len(phiRealesAcortada))
	
	indiceAnterior = None
	
	for indice in indices:	
	
		if(indiceAnterior != None):
			# Calcula cuantas veces debe repetir esa medicion.
			cantidadElementos = indice['indicePPS'] - indiceAnterior['indicePPS']
			# Asigna las repeticiones a la lista.
			asignarElementosLista(	indiceAnterior['indicePPS'] - primeraPosicion, 
									cantidadElementos, 
									phiNTP[indiceAnterior['indiceMedicion']], 
									phiNTPExtendido)
		
		indiceAnterior = indice
		
	cantidadElementos = len(phiRealesAcortada) - indiceAnterior['indicePPS'] 
		
	asignarElementosLista(	indiceAnterior['indicePPS'] - primeraPosicion, 
							cantidadElementos, 
							phiNTP[indiceAnterior['indiceMedicion']], 
							phiNTPExtendido)
							
	return phiRealesAcortada, phiNTPExtendido
		