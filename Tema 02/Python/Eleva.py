#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	Escribir un algoritmo que solicite dous números enteiros e visualice o resultado do primeiro número elevado ao segundo
#
base=input("Base:?")
exp=input("Expoñente:?")
print("O resultado de "+str(base)+ "elevado a "+str(exp)+" é: ")

# Un número elevado a un espoñente negativo e o inverso do expoñente positivo n^-x  = 1 / n^x
#
if (exp < 0):
	print("1/")
	exp=-exp

resultado=1
while (exp > 0):
	resultado = resultado * base
	exp=exp-1

print resultado
