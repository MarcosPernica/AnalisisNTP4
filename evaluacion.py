from bisect import bisect_left
from nucleo import *
import math
import time

# A partir de una indiceInicial devuelve el indiceFinal que esta 'anchoVentana' en segundos mas adelante.
def determinarIndiceFinalIntervalo(phiReales, indiceInicial, anchoVentana):
	tiempoVentana = 0
	indiceFinal = indiceInicial
	
	longitudPhiReales = len(phiReales)
	
	# Va sumando el tiempo, ya que los phiReales son el delta entre dos PPS menos 1 simplemente sumandolos consecutivamente
	# se tiene el delta de todo el intervalo.
	
	while (	tiempoVentana < anchoVentana and 
			indiceFinal < longitudPhiReales):
		tiempoVentana += phiReales[indiceFinal] + 1
		indiceFinal += 1
		
	return indiceFinal
		
# Calcula el MTIE usando el tamaño de la ventana dada y a partir de un tRelativo (al inicio de las mediciones) especifico.
def calcularMTIEIntervalo(inicioVentana, anchoVentana, phiReales, TE, pps):
	
	indiceInicial = bisect_left(pps, inicioVentana)
		
	indiceInicial = determinarIndicePPS(indiceInicial, inicioVentana, inicioVentana, pps)['indicePPS']
	indiceFinal = determinarIndiceFinalIntervalo(phiReales, indiceInicial, anchoVentana)
	
	maximo = max(TE[indiceInicial:indiceFinal])
	minimo = min(TE[indiceInicial:indiceFinal])
	
	return maximo - minimo

# Calcula el MTIE de todo el tiempo de observacion dado.
def calcularMTIE(anchoVentana, phiReales, TE, pps, desplazamientoVentana = 1):

	# Como es el pps se asume que hay un elemento por segundo.
	cantidadElementos = math.floor(len(pps) / desplazamientoVentana)
	MTIE = crearLista(cantidadElementos)
	anchoVentanaMinutos = anchoVentana / 60
	
	for i in range(0, cantidadElementos):
		inicioVentana = i * desplazamientoVentana + pps[0]
		# Para que se puedan comparar los MTIE usando ventanas de diferentes longitudes se divide el MTIE de cada intervalo por
		# la cantidad de minutos que dura esta.
		MTIE[i] = calcularMTIEIntervalo(inicioVentana, anchoVentana, phiReales, TE, pps) / anchoVentanaMinutos 
		
	return MTIE