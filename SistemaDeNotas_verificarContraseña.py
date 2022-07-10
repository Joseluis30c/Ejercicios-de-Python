print("ITANES INSTITUTE")
print("BIENVENIDO AL SISTEMA DE NOTAS EN PYTHON")
print()
contra=input("Ingrese la nueva contraseña: ")
contra2=input("Repita la nueva contraseña de acceso: ")
import os
while True:
	os.system("cls")
	if contra==contra2:
		print("ITANES INSTITUTE")
		print("BIENVENIDO AL SISTEMA DE NOTAS EN PYTHON")
		i=0
		while i<3:
			contra3=(input("Ingrese la contraseña de acceso al Sistema de Notas: "))
			i=i+1
			if contra==contra3:
				os.system("cls")
				print("ITANES INSTITUTE")
				print()
				print("BIENVENIDO AL SISTEMA DE NOTAS EN PYTHON \nMODULO I-REGISTRO DE NOTAS")
				print()
				print("Carreras de Tecnologías de la Informacion: ") 
				print("PBGD = INTERNET DE LAS COSAS Y BIG DATA \nPRID = REDES Y SEGURIDAD INFORMATICA \nPDSD = DESARROLLO DE SOFTWARE \nPRCD = REDES DE COMPUTADORAS Y COMUNICACIÓN DE DATOS \nPSIT = SEGURIDAD DE LA INFORMACIÓN \nPSMD = SOPORTE Y MANTENIMIENTO DE EQUIPOS DE COMPUTACIÓN \nPTID = TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIÓN \nPABD = ADMINISTRACIÓN DE BASE DE DATOS \nPDDW = DISEÑO Y DESARROLLO WEB")
				print()
				codigo=input("Código de carrera: ")
				Calumnos=input("¿Cuántos alumnos desea procesar? ")
				input()
				break
			else:
				print("Contraseña Incorrecta")
				if i==3:
					print("Intentos Agotados")
					break		
	else:
		print("No coinciden las contraseñas")
		input()
		break
	
	
