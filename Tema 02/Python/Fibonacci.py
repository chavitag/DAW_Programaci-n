#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	Escribir un algoritmo que visualice na pantalla o número de términos da serie de Fibonacci que indique o usuario.
#	A serie de Fibonacci ten a seguinte forma:
#	1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

N=input("Cantos termos queres ver?:")
t1 = 1
t2 = 1
while (N > 0):
	print(str(t1)+" ");
	s=t1+t2
	t1=t2
	t2=s
	N=N-1

