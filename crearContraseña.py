nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=input("ingrese su edad: ")
# Creación de una contraseña basada en el nombre y la edad del usuario.
contraseña=nombre.upper()[0]+apellido.upper()[0]+edad+nombre.upper()[-1]+apellido.upper()[-1]
print("su contraseña es ",contraseña)
