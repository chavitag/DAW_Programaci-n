#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# A liña anterior, indica que o ficheiro está en utf-8, para poder usar os acentos
#
# Indica si un número é par ou impar
#
#	Pedir numero
#	Si (o resto de dividir o número entre dous é igual a 0) entón 
#		visualizar "O Número " numero "é Par"
#	Se non 
#		visualizar "O Número " numero "é IMPAR"
#	Fin-Si

num=int(input("Introduce un número: "))
if ( num % 2 == 0):
	print("O Número "+str(num)+" é PAR")
else:
	print("O Número "+str(num)+" é IMPAR")

