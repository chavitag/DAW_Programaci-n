#!/bin/python
# -*- coding: utf-8 -*-
#
# Algoritmo que permita calcular a idade actual de una persona en días, 
# solicitando o ano de nacemento e tendo en conta os anos bisiestos (contando dende o 1 de xaneiro).
#
# Pedir ano
# anoactual=2018
# totaldias=0
# Mentras ano < anoactual
#	Si ano é bisiesto totaldias=totaldias+366
#	SeNon		  totaldias=totaldias+365
#	ano=ano+1
# FinMentras
# Visualizar "Tes " totaldias "días".
#

ano=int(input("Dime o Ano de Nacemento:"))
anoactual=2018
totaldias=0
while(ano<anoactual):
	if ((ano % 4 == 0) and ( (ano % 100 !=0) or (ano%400 == 0) )):
		totaldias=totaldias+366
	else:
		totaldias=totaldias+365
	ano=ano+1
print("Tes "+str(totaldias)+" dias")


