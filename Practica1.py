import ManejoArchivos

def escribir(cad):
	archivo = open('nuevo.txt','a')
	archivo.write(cad)
	archivo.close()

def sumatoria(mx, my,ma,na,it,alf,tt):
	result = 0
	print("valores de teta")
	print(tt)
	print("primer for desde 0 hasta ")
	print(ma)
	print("segundo for desde 0 hasta ")
	print(na)
	print("matriz x")
	print(mx)
	print("matriz y")
	print(my)
	#a = 1 + float(mx[0][0])
	print(a)
	for i in range(ma):
		result = result + tt[0] #teta sub cero
		for j in range(na):
			result = result + tt[j+1]*float(mx[i][j])
		#da como resultado 0 + 0x1 + 0x2 + 0x3
		result = result - float(my[i])
		#sumar toda la fila
		sparcial = 0
		for j in range(na):
			sparcial = sparcial + float(mx[i][j])
		result = result*sparcial
	#da como resultado SUMATORIA(h0(xi) - yi)x(i,j)
	result = (1/ma)*result*float(alf)
	return result

clase = ManejoArchivos.sergio	
def leerArchivo():

	try:
		f = open('archivo.txt',w)
	except:
		print('El archivo no existe')			
print('Escriba la cadena') # pido la cadena :)

cadena = input()

if cadena == "error":
	print('error')
else:
	#print(cadena)
	lista = cadena.split(" ")
	if len(lista) == 5:
		variablesX = lista[0]
		variablesY = lista[1]
		matrizy = clase.leerArchivoY(variablesY)
		matrizx = clase.leerAchivoX(variablesX)
		#print(clase.filasX)
		alfa = lista[2]
		iteraciones = lista[3]
		tolerancia = lista[4]
		teta = []
		a = 2
		m = len(matrizx)
		n = len(matrizx[0])
		teta.append(1) #teta sub cero
		for i in range(len(matrizx[0])):
			teta.append(a)
			#teta[i] = a
			a=a+1
		#print(variablesX + ' ' + variablesY+' '+alfa+' '+ iteraciones+' '+tolerancia+' ')
		#print(matrizx)
		#print(len(matrizx))
		cadena = ""
		for i in range(int(iteraciones)):
			for j in range(len(matrizx[0]) + 1): #recorremos todos los tetas
				teta[j] = teta[j] - sumatoria(matrizx,matrizy,m,n,iteraciones,alfa,teta)
				print('teta' + str(j) + ':  ' + str(teta[j]))
				cadena = cadena + 'teta' + str(j) + ':  ' + str(teta[j]) + '\n'
				#print(j)
				#print(":")
				#print(teta[j])
				if teta[j] < float(tolerancia):
					j = 100000000
					i = 100000000
		print("FIN")
		escribir(cadena)
	else:
		print('cadena de entrada incorrecta!')
		#print(lista)
