p1=int(input("Ingrese la nota de la practica 1: "))
p2=int(input("Ingrese la nota de la practica 2: "))
p3=int(input("Ingrese la nota de la practica 3: "))
ep=int(input("Ingrese la nota del examen parcial: "))
ef=int(input("Ingrese la nota del examen final: "))
pp=(p1+p2+p3)/3
prom=(pp+2*ep+3*ef)/6
print("El promedio de practicas es: ",round(pp,2))
print("El promedio final es: ",round(prom,2))
