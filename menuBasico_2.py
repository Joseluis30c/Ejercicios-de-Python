import os
while True:
	os.system("cls")
	print("Opcion 1 - comenzar programa")
	print("Opcion 2 - Imprimir lista")
	print("Opcion 3 - Terminar programa")
	opcion=int(input("Ingrese la opcion: "))
	if opcion==1:
		print("Iniciando programa")
		input()
	elif opcion==2:
		print("Imprimindo listado")
		print("producto1 \nproducto2 \nproducto3")
		input()
	elif opcion==3:
		print("Terminando programa")
		input()
		break
	else:
		print("Opcion incorrecta ingrese 1, 2 o 3 ")
		input()
