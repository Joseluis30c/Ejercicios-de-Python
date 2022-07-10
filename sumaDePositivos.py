positivos=0
suma=0
num=int(input("Ingrese un numero: "))
while num!=0:
	if num>0:
		positivos+=1
		suma+=num
	num=int(input("Ingrese un numero: "))
print("La suma de os numeros positivos es ",suma)
