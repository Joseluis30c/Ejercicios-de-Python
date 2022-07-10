num=int(input("ingrese un numero entero: "))
contador=0
for i in range(1, num+1):
	if num%i==0:
		contador+=1
if contador==2:
	print("True")
else:
	print("False")




		
