suma=0
num=int(input("Ingrese un numero: "))
# Tomando el número y dividiéndolo por 10 y luego sumando el resto a la suma.
while num!=0:
    digito=num%10
    suma=suma+digito
    num=num//10
print("Suma de los dígitos:", suma)
