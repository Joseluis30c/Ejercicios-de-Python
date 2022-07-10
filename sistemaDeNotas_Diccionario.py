import os
import sys
print("ITANES INSTITUTE")
print("BIENVENIDO AL SISTEMA DE NOTAS EN PYTHON")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
contra=input("Ingrese la nueva contraseña: ")
contra2=input("Repita la nueva contraseña de acceso: ")

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
				diccionario={"PBGD":'"INTERNET DE LAS COSAS Y BIG DATA"'}
				diccionario["PRID"]='"REDES Y SEGURIDAD INFORMATICA"'
				diccionario["PDSD"]='"DESARROLLO DE SOFTWARE"'
				diccionario["PRCD"]='"REDES DE COMPUTADORAS Y COMUNICACIÓN DE DATOS"'
				diccionario["PSIT"]='"SEGURIDAD DE LA INFORMACIÓN"'
				diccionario["PSMD"]='"SOPORTE Y MANTENIMIENTO DE EQUIPOS DE COMPUTACIÓN"'
				diccionario["PTID"]='"TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIÓN"'
				diccionario["PABD"]='"ADMINISTRACIÓN DE BASE DE DATOS"'
				diccionario["PDDW"]='"DISEÑO Y DESARROLLO WEB"'
				diccionario["pbgd"]='"INTERNET DE LAS COSAS Y BIG DATA"'
				diccionario["prid"]='"REDES Y SEGURIDAD INFORMATICA"'
				diccionario["pdsd"]='"DESARROLLO DE SOFTWARE"'
				diccionario["prcd"]='"REDES DE COMPUTADORAS Y COMUNICACIÓN DE DATOS"'
				diccionario["psit"]='"SEGURIDAD DE LA INFORMACIÓN"'
				diccionario["psmd"]='"SOPORTE Y MANTENIMIENTO DE EQUIPOS DE COMPUTACIÓN"'
				diccionario["ptid"]='"TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIÓN"'
				diccionario["pabd"]='"ADMINISTRACIÓN DE BASE DE DATOS"'
				diccionario["pddw"]='"DISEÑO Y DESARROLLO WEB"'
				os.system("cls")
				print("ITANES INSTITUTE")
				print("BIENVENIDO AL SISTEMA DE NOTAS EN PYTHON")
				print("CARRERAS DE TECNOLOGÍAS DE LA INFORMACIÓN\
				\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
				\nPBGD=INTERNET DE LAS COSAS Y BIG DATA\
				\nPRID=REDES Y SEGURIDAD INFORMATICA\
				\nPDSD=DESARROLLO DE SOFTWARE\
				\nPRCD=REDES DE COMPUTADORAS Y COMUNICACIÓN DE DATOS\
				\nPSIT=SEGURIDAD DE LA INFORMACIÓN\
				\nPSMD=SOPORTE Y MANTENIMIENTO DE EQUIPOS DE COMPUTACIÓN\
				\nPTID=TECNOLOGÍAS DE LA INFORMACIÓN Y COMUNICACIÓN\
				\nPABD=ADMINISTRACIÓN DE BASE DE DATOS\
				\nPDDW=DISEÑO Y DESARROLLO WEB")
				codigo=input("\nIngrese el codigo de su carrera:  ")
				print("La carrera es",diccionario[codigo])
				alumno=0
				idss=[]
				nombres=[]
				apellidos=[]
				nf=[]
				alumnos=int(input("Cuantos Alumnos Deseas Ingresar: "))
				os.system("cls")
				for i in range(alumnos):
					print("ITANES INSTITUTE")
					print("BIENVENIDO AL SISTEMA DE NOTAS EN PYTHON")
					print("CARRERA: ",diccionario[codigo])
					print()
					print("MODULO I-REGISTRO DE NOTAS")
					while alumno<alumnos:
						alumno+=1
					print("REGISTRO N°0"+str(alumno))
					ids=input("ID: ")
					idss.append(ids)
					apellido=input("apellido: ")
					apellidos.append(apellido)
					nombre=input("nombre ")
					nombres.append(nombre)
					print("NOTA FINAL: ")
					MAT=int(input("MATEMATICA: "))
					LEN=int(input("LENGUAJE Y COMUNICACION: "))
					ITI=int(input("INTRODUCCION A LAS TECNOLOGIAS DE LA INFORMACIÓN: "))
					DTC=int(input("DIBUJO TECNICO CON CAD: "))
					FYQ=int(input("FISICA Y QUIMICA: "))
					DPYTL=int(input("DESARROLLO PERSONAL Y TALLER DE LIDERAZGO: "))
					CDPI=int(input("COMPETENCIAS DIGITALES: "))
					ING=int(input("INGLES: "))
					nt=(MAT+LEN+ITI+DTC+FYQ+DPYTL+CDPI+ING)/8
					nf.append(nt)
					os.system("cls")
				c=0
				for k in range(c,alumnos):
					print("RESUMEN:")
					print("SISTEMA DE NOTAS 'ITANES'")
					print("CARRERA: ",diccionario[codigo])
					print("MODULO I-REGISTRO DE NOTAS")
					print(idss[c],apellidos[c],nombres[c], nf[c], sep="  ")
					c=c+1
					print()
					print("Enter para ver siguiente")
					input()
					continue
			else:
				import sys
				print("Contraseña Incorrecta")
				if i==3:
					print("Intentos Agotados")
					sys.exit()			
	else:
		print("No coinciden las contraseñas")
		input()
		break
				
