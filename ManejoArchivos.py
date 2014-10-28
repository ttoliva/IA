class sergio:
	filasX = 0
	
	def leerAchivoX(archivo):
		contador = 0
		matrizX = []
		try:
			archivoX=open(archivo,'r')
			linea=archivoX.readline()
			linea = linea.replace("\n", "")
			listaTX = linea.split(",") 
			cantidadX = len(listaTX) 
			for i in range(sergio.filasX):
				matrizX.append([])
				for j in range(cantidadX):
					matrizX[i].append(None)
					
			i = 0;
			for x in listaTX:								
				matrizX[0][i] = x
				i = i + 1
				
		
			while linea!="":
				contador = contador + 1
				#print(linea)
				linea=archivoX.readline()
				linea = linea.replace("\n", "")
				listaTX = linea.split(",")
				i = 0;
				if contador < sergio.filasX:
					for x in listaTX:								
						matrizX[contador][i] = x
						i = i + 1
			archivoX.close()
		except:
			print('archivo no existe '+ archivo)			
		return matrizX
		
		
	def leerArchivoY(archivo1):
		archivoY=open(archivo1,'r')
		lineaY=archivoY.readline() 
		listaY = []
		while lineaY!="":			
			#print(lineaY)
			lineaY = lineaY.replace("\n", "")
			listaY.append(lineaY)
			lineaY=archivoY.readline()			
		archivoY.close()
		sergio.filasX = len(listaY)
		return listaY
