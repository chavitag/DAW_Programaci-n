#!/bin/bash

# Nos scripts, as liñas que comenzan por # son comentarios salvo a primeira coa
# admiración que indica qué intérprete se debe utilizar.

#  PSEUDOCÓDIGO
#
#	Visualizar "Introduce un número: "
#	Pedir num
#	Si (num >= 0)
#		r=1
#		Visualizar "Calculando " num "!"
#		Mientras num > 0 
#			r = r * num
#			num = num - 1
#		Fin-Mientras
#		Visualizar "O factorial é " r
#	Si Non
#		Visualizar "Non se poden calcular factoriais de números negativos"
#	FinSi


echo "Introduce un número: "
read num
if [ $num -ge 0]; then
	r=1
	echo "Calculando $num! ..."

	while [ $num -gt 0 ]; do
	# let r=r*num
	 r=$((r*num))
	# let num=num-1
	 num=$((num-1))
	done
	echo "O factorial é $r"
else
	echo "Non se poden calcular factoriais de números negativos"
fi
