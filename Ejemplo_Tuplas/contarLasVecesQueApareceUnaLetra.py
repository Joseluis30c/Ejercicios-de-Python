a=input("Introduce una palabra: ")
# Contar el número de veces que aparece una letra en una palabra.
letra=('a')
for i in letra:
	c=0
	for j in a:
		if j==i:
			c+=1
	print("La vocal" ,i, "aparece",c," veces")
