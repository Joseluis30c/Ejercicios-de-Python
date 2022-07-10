# Pidiéndole al usuario que ingrese un número y luego agregará el número al total. Seguirá pidiéndole
# al usuario que ingrese un número hasta que el usuario ingrese 0.
total=0
num=int(input("Ingrese un numero: "))
while num != 0:
	total+=num
	num=int(input("Ingrese un numero: "))
print("Suma de los numeros es ",total)
