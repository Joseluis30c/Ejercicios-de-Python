nombre=input("¿Cual es su nombre? ")
edad=input("¿Cuántos años tienes? ")
direccion=input("Ingrese su dirección: ")
cel=input("¿Cuál es tu número de telefono? ")
diccionario={"nombre": nombre, "edad": edad, "direccion": direccion, "cel": cel}
print(diccionario["nombre"], "tiene" ,diccionario["edad"], "años, vive en", diccionario["direccion"], "y su número de teléfono es", diccionario["cel"])
