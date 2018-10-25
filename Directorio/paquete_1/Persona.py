class Docente:
	def __init__(self,n,a):
		self.nombre = n
		self.ciudad = a
	def setnombre(self,n):
		self.nombre = n
	def setciudad(self,a):
		self.ciudad = a
	def getnombre(self):
		return self.nombre
	def getciudad(self):
		return self.ciudad
	def presentarD (self):
		cadena = "%s\n\t%s" % (self.nombre,self.ciudad)

class Estudiante:

	def __init__(self,  n, lista_docentes):
		self.nombres = n
		self.docentes = lista_docentes
	def setnombres(self, n):
		self.nombres = n
	def setdocentes(self,lista_docentes):
		for i in (len(lista_docentes)):
			self.docentes = lista_docentes
	def getnombres(self):
		return self.nombres
	def getdocentes(self):
		return self.docentes
	def presentarD (self):
		cadena = "Estudiante : %s\n" % (self.getnombres())
		cadena = "%s%s\n" % (cadena,"Lista de docentes:")
		for i in range (len(self.docentes)):
			cadena = "%s\n%s---%s" % (cadena,self.docentes[i].getnombre(),self.docentes[i].getciudad())
		return cadena
