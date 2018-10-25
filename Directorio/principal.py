from paquete_1.Persona import * #importamos el paquete 

d = Docente("Docente B D","Loja") #variable con los datos  para docente
d2 = Docente("Docente Pray","Quito")
listado = [d,d2] #esas variables  metemos en una lista 
e = Estudiante("Luis",listado) #llamamos al metodo estudiante con  los datos "luis" y la lista
print(e.presentarD()) #presentamos de  la clase estudiante