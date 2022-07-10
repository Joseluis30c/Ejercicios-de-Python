pares=0
num=int(input("Ingrese un numero: "))
while num!=-1:
    if num%2==0:
        pares+=1
    suma=0
    while num!=0:
        digito=num%10
        suma+=digito
        num=num//10
    print("La suma de sus digitos es", suma)
    num=int(input("Ingrese un numero: "))
print("Se ingresaron", pares, "numeros pares")
