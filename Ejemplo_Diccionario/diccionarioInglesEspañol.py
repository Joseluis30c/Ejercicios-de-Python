dictionario={}
a=input("Introduce la palabra en español e ingles (español:ingles) separadas por comas: ")
# Dividir la entrada por comas y luego dividir la clave y el valor por dos puntos.
for i in a.split(','):
    key,value=i.split(':')
    dictionario[key] = value
b=input('Introduce una frase en español: ')
# Comprueba si la palabra está en el diccionario y si lo está, imprime la traducción. Si no es así,
# imprime la palabra.
for i in b.split():
    if i in dictionario:
        print(dictionario[i], end=' ')
    else:
        print(i, end=' ')
