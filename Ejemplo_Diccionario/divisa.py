variable={'Soles':'S/.', 'Dollar':'$','Euro':'€', 'Yen':'¥'}
a=input("Ingrese una divisa: ")
# Imprimiendo el valor de la clave `a.title()` si existe, en caso contrario imprime `"La divisa no es
# correcta"`
print(variable.get(a.title(), "La divisa no es correcta"))
