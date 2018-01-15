# -*- coding: utf-8 -*-

import os

print ('''
\033[1;32m************************Python Git************************\033[1;m
\033[1;32m Author: Marco Argueta\033[1;m
		''')

try:

	ubicacion = str(input("\033[1;32mDigite la ubicación del proyecto: \033[1;m"))
	os.chdir(ubicacion)

	print("Selecciona la opción que deseas realizar")

	def inicio():
		while True:
			print("""
1) Git Init (Solo primera vez)
2) Git Add
3) Git Commit -m mensaje
4) Git remote add origin (Solo primera vez)
5) Git push origin master
*) Ctrl + c para salir
				""")
			
			opcion = input("\033[1;32mSeleccione opción: \033[1;m")

			while opcion == "1":
				print("Comando a ejecutar: git init ")
				os.system("git init")
				regresar = input("\033[1;32m¿Regresar al menú principal (si/no)? \033[1;m")
				if regresar != "no":
					os.system("clear")
					inicio()

			while opcion == "2":
				print("Comando a ejecutar: git add .")
				os.system("git add . " + ubicacion)
				regresar = input("\033[1;32m¿Regresar al menú principal (si/no)? \033[1;m")
				if regresar != "no":
					os.system("clear")
					inicio()

			while opcion == "3":
				mensaje = input("Escriba el mensaje del commit: ")
				print("Comando a ejecutar: git commit -m \"" + mensaje + "\"")
				os.system("git commit -m \"" + mensaje + " \"")
				regresar = input("\033[1;32m¿Regresar al menú principal (si/no)? \033[1;m")
				if regresar != "no":
					os.system("clear")
					inicio()

			while opcion == "4":
				origen = input("Escribe el origen del repositorio: ")
				print("Comando a ejecutar: git remote add origin " + origen)
				os.system("git remote add origin " + origen)
				regresar = input("\033[1;32m¿Regresar al menú principal (si/no)? \033[1;m")
				if regresar != "no":
					os.system("clear")
					inicio()

			while opcion == "5":
				print("Comando a ejecutar: git push origin master")
				os.system("git push origin master")
				regresar = input("\033[1;32m¿Regresar al menú principal (si/no)? \033[1;m")
				if regresar != "no":
					os.system("clear")
					inicio()

	inicio()

except KeyboardInterrupt:
	print(" Fin del programa. Adiós")
