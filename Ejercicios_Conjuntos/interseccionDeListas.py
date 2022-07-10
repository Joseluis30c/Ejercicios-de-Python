#ejercicio 4 		#INTERSECCION DE CONJUNTOS

a=input("ingrese un numero de 4 digitos: ")
b=input("ingrese otro numero de 4 digitos: ")
# Creando un conjunto de la lista ayb y luego tomando la intersección de los dos conjuntos.
conjunto=set(a)
conjunto2=set(b)
c=conjunto&conjunto2
print("Sus numeros en comun son ",c)
