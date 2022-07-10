num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
num3=int(input("Ingresa el tercer numero: "))
if num1<=num2 and num1<=num3:
	menor=num1
	if num2<=num3:
		medio=num2
		mayor=num3
	else:
		medio=num3
		mayor=num2
elif num2<=num1 and num2<=num3:
	menor=num2
	if num1<=num3:
		medio=num1
		mayor=num3
	else:
		medio=num3
		mayor=num1
else:
	menor=num3
	if num1<=num2:
		medio=num1
		mayor=num2
	else:
		medio=num2
		mayor=num1
print(menor,medio,mayor)
