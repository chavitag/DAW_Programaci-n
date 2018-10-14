#!/bin/sh
##
## División mediante Restas
##

##
## 	Supoñemos que o resultado é positivo
##
#	signo=1

#	Visualizar "Dividendo?: "
#	Pedir dividendo
##
## Si o dividendo é negativo, o resultado é negativo, e facemos os cálculos coma si fora positivo
##
#	Si (dividendo < 0) 
#		signo = -1
#		dividendo = -dividendo
#	Fin-Si

#	Visualizar "Divisor?: "
#	Pedir divisor

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


signo=1
echo "Dividendo?: "
read dividendo

# Si o dividendo é negativo, o resultado é negativo, e facemos os cálculos coma si fora positivo
if [ $dividendo -lt 0 ]; then
  signo=-1
  dividendo=$((dividendo*-1))
fi

echo "Divisor?: "
read divisor

if [ $divisor -eq 0 ]; then
	echo "Non se pode realizar unha división entre 0"
else
##	Si o divisior é negativo, cambia o signo do resultado, facemos o cálculo como si fora positivo
	if [ $divisor -lt 0 ]; then
	  signo=$((signo*-1))
	  divisor=$((divisor*-1))
	fi
   cociente=0
## [ $dividendo -ge $divisor ], o divido para amosar o operador lóxico || (ou)
	while [ $dividendo -gt $divisor ] || [ $dividendo -eq $divisor ]; do
		dividendo=$((dividendo-divisor))
		cociente=$((cociente+1))
	done
	dividendo=$((dividendo*signo))
	cociente=$((cociente*signo))
	echo "O resultado é Cociente: $cociente e Resto: $dividendo"
fi

