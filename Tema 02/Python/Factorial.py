#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Cálculo do factorial dun número

num=input("Introduce un número: ")
if (num >= 0):
	r=1
	print("Calculando "+str(num)+"!")
	while (num > 0 ):
		r = r * num
		num = num - 1
	print("O factorial é "+str(r))
else:
	print("Non se poden calcular factoriais de números negativos")
