class Docente: #Clase docente
	def __init__(self,n,a): # se define el __init__  con las variables a utilizar
		self.nombre = n
		self.ciudad = a
	def setnombre(self,n): # agregamos la variable nombre
		self.nombre = n
	def setciudad(self,a): #agregamos la variable ciudad
		self.ciudad = a
	def getnombre(self): #obtener nombre (retorna el valor)
		return self.nombre
	def getciudad(self): # obtener ciudad (retorna el valor)
		return self.ciudad
	def presentarD (self): #funcion presentar datos
		cadena = "%s\n\t%s" % (self.nombre,self.ciudad)

class Estudiante: #Clase estudiante

	def __init__(self,  n, lista_docentes): #se define el __init__  con las variables a utilizar
		self.nombres = n
		self.docentes = lista_docentes
	def setnombres(self, n): # agregar nombres
		self.nombres = n
	def setdocentes(self,lista_docentes):# agregamos docentes (lista)
			self.docentes = lista_docentes
	def getnombres(self): #obtener nombres
		return self.nombres
	def getdocentes(self): #obtener docentes
		return self.docentes
	def presentarD (self): #presentamos 
		cadena = "Estudiante : %s\n" % (self.getnombres()) #cadena donde nos presenta el nombre del estudiante
		cadena = "%s%s\n" % (cadena,"Lista de docentes:")
		for i in range (len(self.docentes)):
			cadena = "%s\n%s---%s" % (cadena,self.docentes[i].getnombre(),self.docentes[i].getciudad()) #cadena donde nos presenta el nombre y cuidad de cada docente
		return cadena
