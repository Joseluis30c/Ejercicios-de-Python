nom1=input("Ingrese un nombre: ")
nom2=input("Ingrese otro nombre: ")
# Comprobando si la primera letra del primer nombre es la misma que la primera letra del segundo
# nombre o si la última letra del primer nombre es la misma que la última letra del segundo nombre.
if nom1[0]==nom2[0] or nom1[-1]==nom2[-1]:
	print("coincidencia")
else:
	print("No hay coincidencia")

