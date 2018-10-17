#!/usr/bin/python
# -*- coding: utf-8 -*-
##
## División mediante Restas
##

##
## 	Supoñemos que o resultado é positivo
##
#	signo=1
#
#	Visualizar "Dividendo?: "
#	Pedir dividendo
##
## Si o dividendo é negativo, o resultado é negativo, e facemos os cálculos coma si fora positivo
##
#	Si (dividendo < 0) 
#		signo = -1
#		dividendo = -dividendo
#	Fin-Si
#
#	Visualizar "Divisor?: "
#	Pedir divisor
#
#	Si (divisor == 0)
#		Visualizar "Non se pode realizar unha división entre 0"
#	Si-Non
##
##	Si o divisior é negativo, cambia o signo do resultado, facemos o cálculo como si fora positivo
##
#	Si (divisor < 0) 
#			signo = -signo
#			divisor = -divisor
#		fin-Si
#
#		cociente = 0
#		Mientras dividendo >= divisor
#			dividendo = dividendo - divisor
#			cociente = cociente + 1
#		Fin-Mentras
##
##	Axustamos o signo
##
#     dividendo=dividendo*signo
#     cociente=cociente*signo
#		Visualizar "O resultado é Cociente: " cociente " e Resto: " dividendo
#	Fin-Si

signo=1;
dividendo=int(input("Dividendo?: "))

# Si o dividendo é negativo, o resultado é negativo, e facemos os cálculos coma si fora positivo
if ( dividendo < 0 ):
	signo=-1
	dividendo=dividendo*-1

divisor=int(input("Divisor?: "))

if ( divisor == 0 ):
	print("Non se pode realizar unha división entre 0")
else:
	##	Si o divisior é negativo, cambia o signo do resultado, facemos o cálculo como si fora positivo
	if ( divisor < 0 ): 
		signo=signo*-1
		divisor=divisor*-1
   
	cociente=0
	while ( dividendo >= divisor ):
		dividendo=dividendo-divisor
		cociente=cociente+1

	## axustamos o signo
	dividendo=dividendo*signo;
	cociente=cociente*signo;
	print("O resultado é Cociente: "+str(cociente)+" e Resto: "+str(dividendo))
