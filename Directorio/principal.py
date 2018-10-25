from paquete_1.Persona import *

d = Docente("Docente B D","Loja")
d2 = Docente("Docente Pray","Quito")
listado = [d,d2]
e = Estudiante("Luis",listado)
print(e.presentarD())