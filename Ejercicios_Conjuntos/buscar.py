#ejercicio 2 	#Pertenencia
print("INGRESE LOS DATOS SEPARADOS CON LA TECLA ESPACIO")
print()
a=("JOSE","PEDRO", "JUAN", "JEFERSON", "LUIS", "CARLOS")
print("Nombres HOMBRES: JOSE, PEDRO, JUAN, JEFERSON, LUIS Y CARLOS")
b=input("NOMBRE A BUSCAR: ")
conjunto=set(a)
conjunto2=set(b)
if b in conjunto:
	print("Si esta")
else:
	print("No esta")
