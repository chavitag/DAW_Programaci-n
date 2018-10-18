#!/bin/python
# -*- coding: utf-8 -*-
#
#	Determiña cal de dous números é o maior
#
# Pedir num1
# Pedir num2
# Si (num1 >  num2) Visualizar "O maior é " num1
# SeNon	Si (num2 > num1) Visualizar "O maior é " num2
# SeNon Visualizar "Son Iguais"
num1=int(input("Introduce un numero:"))
num2=int(input("Introduce otro numero:"))
if (num1>num2):
	print(str(num1)+" e maior que "+str(num2))
else:
	if (num2>num1):
		print(str(num2)+" e maior que "+str(num1))
	else:
		print("Son Iguais")

