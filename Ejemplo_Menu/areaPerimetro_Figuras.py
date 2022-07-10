import os
def cuadrado():
	os.system("cls")
	print("----CUADRADO----")
	print("1. Perimetro")
	print("2. Area")
	print("3. Regresar")
	a=int(input("Dame una opcion: "))
	if a==1:
		os.system("cls")
		print("----Perimetro del Cuadrado----")
		lado=int(input("Ingrese el valor del lado: "))
		peri=lado*4
		print("El perimetro es", peri )
		input()
	elif a==2:
		os.system("cls")
		print("----Area del Cuadrado----")
		lado1=int(input("Ingrese el valor del lado: "))
		area=lado1*lado1
		print("El Area es", area)
		input()
def circulo():
	os.system("cls")
	print("----CIRCULO----")
	print("1. Perimetro")
	print("2. Area")
	print("3. Regresar")
	a=int(input("Dame una opcion: "))
	if a==1:
		os.system("cls")
		print("----Perimetro del Circulo----")
		radio=int(input("Ingrese el valor del radio: "))
		peri=2*3.14*radio
		print("El perimetro es", peri )
		input()
	elif a==2:
		os.system("cls")
		print("----Area del Cuadrado----")
		radio1=int(input("Ingrese el valor del radio: "))
		areac=3.14*(radio1**2)
		print("El Area es", areac)
		input()
def rectangulo():
	os.system("cls")
	print("----RECTANGULO----")
	print("1. Perimetro")
	print("2. Area")
	print("3. Regresar")
	a=int(input("Dame una opcion: "))
	if a==1:
		os.system("cls")
		print("----Perimetro del Rectangulo----")
		base=int(input("Ingrese el valor de la base: "))
		altu=int(input("Ingrese el valor de la altura: "))
		peri=2*(base+altu)
		print("El perimetro es", peri )
		input()
	elif a==2:
		os.system("cls")
		print("----Area del Rectangulo----")
		base=int(input("Ingrese el valor de la base: "))
		altu=int(input("Ingrese el valor de la altura: "))
		area=base*altu
		print("El Area es", area)
		input()
def triangulo():
	os.system("cls")
	print("----Triangulo----")
	print("1. Perimetro")
	print("2. Area")
	print("3. Regresar")
	a=int(input("Dame una opcion: "))
	if a==1:
		os.system("cls")
		print("----Perimetro del Triangulo----")
		lado1=int(input("Ingrese el valor del lado 1: "))
		lado2=int(input("Ingrese el valor del lado 2: "))
		lado3=int(input("Ingrese el valor del lado 3: "))
		peri=lado1+lado2+lado3
		print("El perimetro es", peri )
		input()
	elif a==2:
		os.system("cls")
		print("----Area del Triangulo----")
		base=int(input("Ingrese el valor de la base: "))
		altu=int(input("Ingrese el valor de la altura: "))
		area=(base*altu)/2
		print("El Area es", area)
		input()
def rombo():
	os.system("cls")
	print("----ROMBO----")
	print("1. Perimetro")
	print("2. Area")
	print("3. Regresar")
	a=int(input("Dame una opcion: "))
	if a==1:
		os.system("cls")
		print("----Perimetro del ROMBO----")
		lado=int(input("Ingrese el valor del lado: "))
		peri=lado*4
		print("El perimetro es", peri )
		input()
	elif a==2:
		os.system("cls")
		print("----Area del ROMBO----")
		lado1=int(input("Ingrese el valor de la diagonal mayor: "))
		lado2=int(input("Ingrese el valor de la diagonal menor: "))
		area=(lado1*lado2)/2
		print("El Area es", area)
		input()
def trapecio():
	os.system("cls")
	print("----TRAPECIO----")
	print("1. Perimetro")
	print("2. Area")
	print("3. Regresar")
	a=int(input("Dame una opcion: "))
	if a==1:
		os.system("cls")
		print("----Perimetro del TRAPECIO----")
		lado=int(input("Ingrese la suma de sus bases: "))
		ladoo=int(input("Ingrese la suma de sus lados oblicuos: "))
		peri=lado+ladoo
		print("El perimetro es", peri )
		input()
	elif a==2:
		os.system("cls")
		print("----Area del TRAPECIO----")
		lado1=int(input("Ingrese el valor de la base mayor "))
		lado2=int(input("Ingrese el valor de la base menor: "))
		lado3=int(input("Ingrese el valor de la altura: "))
		area=((lado1+lado2)*lado3)/2
		print("El Area es", area)
		input()
def salir():
	if op==7:
		exit
op=0
while op!=7:
	os.system("cls")
	print("Figuras Geometricas")
	print("1. Cuadrado")
	print("2. Circulo")
	print("3. Rectangulo")
	print("4. Triangulo")
	print("5. Rombo")
	print("6. Trapecio")
	print("7. Salir")
	op=int(input("Dame una opcion: "))
	if op==1:
		cuadrado()
	elif op==2:
		circulo()
	elif op==3:
		rectangulo()
	elif op==4:
		triangulo()
	elif op==5:
		rombo()
	elif op==6:
		trapecio()
	else:
		salir()

	
