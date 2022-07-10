while True:
    print("Opcion 1 = comenzar programa")
    print("Opcion 2 = imprimir listado")
    print("Opcion 3 = finalizar programa")
    opcion=int(input("Elige una opcion: "))
    if opcion==1:
        print("Iniciando el programa")
    elif opcion==2:
        print("Imprimiendo listado")
    elif opcion==3:
        print("Finalizando...")
        break
    else:
        print("Opcion incorrecta")
