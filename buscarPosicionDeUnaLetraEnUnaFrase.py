frase=input("Escriba una frase: ")
letra=input("¿Cual es la letra a buscar? : ")
posicion=0
# Comprobando si la posición no es igual a la longitud de la frase.
while posicion!=len(frase):
    # Comprobando si la posición no es igual a la letra en la posición.
    if posicion!=frase[posicion]:
        print("No se encontró en la posición", posicion)
        posicion+=1
        continue
    print("Se encontró en la posición", posicion)
    break
    
