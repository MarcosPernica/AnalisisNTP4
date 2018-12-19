def obtenerPPS(nombreArchivo):
	pps = []
	phiReales = []
	guardarResultados = True
	
	ppsAnterior = None;
	ppsActual = None;
	
	# Umbral por encima del cual se considera erroneo el phiReal (el GPS se desincronizo) y no se guarda.
	umbral = 1e-4
	
	with open(nombreArchivo) as archivo:
		for linea in archivo:
            
            # Salta las lineas iniciales.
			if not linea[0].isdigit():
				continue
				
			linea = linea[:-1]
			ppsActual = float(linea)
			
			# No se puede calcular el phiReal del primer elemento.
			if ppsAnterior != None:
				phiReal = abs(ppsActual - ppsAnterior - 1)
				
				# Esta maquina de estados tiene por objetivo no guardar los phiReal mas alejados que 'umbral'.
				if(guardarResultados == False and phiReal <= umbral):
					guardarResultados = True
				elif (guardarResultados == True and phiReal > umbral):
					guardarResultados = False
				
				if(guardarResultados == True):
					pps.append(ppsActual)
					phiReales.append(phiReal)

			ppsAnterior = ppsActual
			
	return pps, phiReales

def obtenerMediciones(nombreArchivo):
	phisNTP = []
	tiempos = []
	rtts = []
	
	with open(nombreArchivo) as archivo:
		for linea in archivo:
			# Retirar \n
			linea = linea[:-1]

			# Saltear las lineas de encabezado
			if not linea[0].isdigit():
				continue

			# Desempacar los datos
			t1, t2, t3, t4, phiNTP = linea.split(',')
			
			t1 = float(t1);
	
			tiempos.append(t1)
			phisNTP.append(float(phiNTP))
			rtts.append(float(t4) - float(t1))
			
			
	return tiempos, phisNTP, rtts
