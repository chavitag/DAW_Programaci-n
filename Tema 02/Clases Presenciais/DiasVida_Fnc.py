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
#	Si ano NON é bisiesto totaldias=totaldias+365
#	SeNon		  totaldias=totaldias+366
#	ano=ano+1
# FinMentras
# Visualizar "Tes " totaldias "días".
#
def bisiesto(ano):
	if ((ano % 4 == 0) and ( (ano % 100 !=0) or (ano%400 == 0) )):
		return True
	else:
		return False


ano=int(input("Dime o Ano de Nacemento:"))
anoactual=2018
totaldias=0
while(ano<anoactual):
	if (bisiesto(ano) is False):
		totaldias=totaldias+365
	else:
		totaldias=totaldias+366
	ano=ano+1
print("Tes "+str(totaldias)+" dias")
