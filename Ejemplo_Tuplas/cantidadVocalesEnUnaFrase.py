a=input("Introduce una palabra: ")
# Un bucle for que itera a través de la cadena "vocales" y compara cada letra con la cadena "a" y
# cuenta el número de veces que aparece cada letra en la cadena "a".
vocales=("a","e","i","o","u")
for i in vocales: 
    c=0
    for j in a: 
        if j==i:
            c+=1
    print("La vocal "+i+" aparece "+str(c)+" veces")
