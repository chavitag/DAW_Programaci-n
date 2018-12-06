#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Escribir un algoritmo que visualice os factores primos dun número
#
numero=input("Introduce un número: ")
print("1")
primo=2 
while (numero>1):
	if (numero % primo == 0):
		print primo
		numero = numero / primo
	else:
		primo = primo + 1
