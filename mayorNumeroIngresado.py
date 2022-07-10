# El código le pide al usuario que ingrese un número y
# luego comparará el número con el número
# anterior. Si el número es mayor que el número anterior, 
# se almacenará como el nuevo número mayor.
mayor=-1
num=int(input("Ingresa un numero positivo: "))
while num>=0:
	if num>mayor:
		mayor=num
	num=int(input("Ingresa un numero positivo: "))
print("El mayor numero ingresado es: ",mayor)
