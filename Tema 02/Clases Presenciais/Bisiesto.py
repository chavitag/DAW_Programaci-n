#!/bin/python
# -*- coding: utf-8 -*-
#
# Indica si un ano é bisiesto
#
# Pedir ano
# Si (é divisible por 4) E (non é divisible por 100 OU é divisible por 400) Visualizar "Bisiesto"
# Se Non Visualizar "NON Bisiesto"
ano=int(input("Dime o Ano:"))
if ((ano % 4 == 0) && ( (ano % 4 !=0) || (ano%400 == 0) )):
	print("O ano "+str(ano)+" non é bisiesto")
else:
	print("O ano "+str(ano)+" é bisiesto")

