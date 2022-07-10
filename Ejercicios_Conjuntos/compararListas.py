#ejercicio 1   	IGUALDAD
print("INGRESE LOS DATOS SEPARADOS CON LA TECLA ESPACIO")
print()
colores=input("Lista de colores: ")
colores2=input("Lista de colores: ")
conjunto=set(colores)
conjunto2=set(colores2)
if conjunto==conjunto2:
	print("Ambas listas son Iguales")
else:
	print("Las listas son Diferentes")

